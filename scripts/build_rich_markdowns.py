#!/usr/bin/env python3
"""从 deep/enriched_catalog.json + deep/readmes/ 生成带 README 内容的 rich markdown。
输出 deep/markdowns/{stored_name}.md + SQL UPDATE 文件。
stored_name 的生成与 server/tools/seed_skills.js 保持完全一致。"""
import json, hashlib, os, time
from pathlib import Path

BASE = Path(__file__).parent
DEEP = BASE / "deep"
READMES = DEEP / "readmes"
OUTDIR = DEEP / "markdowns"
OUTDIR.mkdir(parents=True, exist_ok=True)

CATALOG = DEEP / "enriched_catalog.json"
SQL_FILE = DEEP / "update_sizes.sql"
MAX_README_CHARS = 15000  # max README chars in markdown (avoid huge files)


def sha1(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()


def esc(v):
    return str(v or '').replace('|', '\\|').replace('\n', ' ')


def build_markdown(s, cat_key, readme_content):
    rm = ''
    if readme_content:
        truncated = len(readme_content) > MAX_README_CHARS
        body = readme_content[:MAX_README_CHARS]
        if truncated:
            body += '\n\n> *（内容过长，已截断前 {} 字符。完整文档见原链接）*'.format(MAX_README_CHARS)
        # Indent code blocks to fit within the section
        rm = '\n## README / Skill 文档\n\n' + body + '\n'

    return f'''# {s['name']}

> {s['desc'] or '暂无描述。'}

## 基本信息

| 字段 | 内容 |
|---|---|
| 名称 | {esc(s['name'])} |
| 链接 | {esc(s['url'])} |
| 来源聚合 | {esc(s.get('group', '') or '未知')} |
| 分类路径 | {esc(cat_key)} |
| 类型 | AI Skill / Agent Tool |

## 简介

{s['desc'] or '暂无简介。'}
{rm}
## 参考链接

- {s['url']}
'''


def main():
    with open(CATALOG, 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    # Flatten
    skills = []
    def walk(node, keys):
        if not node:
            return
        if node.get('leaf'):
            for it in node.get('items', []):
                it['_cat_path'] = ' / '.join(keys)
                skills.append(it)
            return
        for k in node.get('children', {}):
            walk(node['children'][k], keys + [k])
    for b in catalog['boards']:
        walk(b['data'], [b['name']])

    total = len(skills)
    print(f'Total skills in enriched catalog: {total}')

    sql_lines = []
    with_readme = 0
    without_readme = 0

    for i, s in enumerate(skills):
        cat_key = s['_cat_path']
        name = s['n']
        url = s['u']

        # Compute same IDs as seed_skills.js
        id_seed = cat_key + '\x01' + name + '\x01' + url
        file_id = 'seed-file-' + sha1(id_seed)
        share_id = 'seed-share-' + sha1(id_seed)
        stored = sha1(file_id) + '.md'

        # Read README content if available
        readme_content = ''
        readme_file = s.get('readme_file', '')
        if readme_file:
            rpath = BASE / readme_file
            if rpath.exists():
                try:
                    readme_content = rpath.read_text(encoding='utf-8')
                    with_readme += 1
                except:
                    without_readme += 1
            else:
                without_readme += 1
        else:
            without_readme += 1

        # Generate markdown
        md = build_markdown({'name': name, 'url': url, 'desc': s.get('d', '') or '', 'group': s.get('g', '')}, cat_key, readme_content)

        # Write
        out_path = OUTDIR / stored
        out_path.write_text(md, encoding='utf-8')

        size = len(md.encode('utf-8'))
        # SQL: UPDATE files SET size = X WHERE id = 'Y'
        sql_lines.append(f"UPDATE files SET size = {size} WHERE id = '{file_id}';")

        if (i + 1) % 200 == 0:
            print(f'  {i+1}/{total} markdowns generated ({with_readme} with README, {without_readme} without)')

    # Write SQL
    with open(SQL_FILE, 'w', encoding='utf-8') as f:
        f.write('BEGIN;\n')
        f.write('\n'.join(sql_lines))
        f.write('\nCOMMIT;\n')

    print(f'\nDone! {total} markdowns → {OUTDIR}')
    print(f'With README: {with_readme} | Without: {without_readme}')
    print(f'SQL update file: {SQL_FILE} ({len(sql_lines)} statements)')

    # Also output a summary
    summary = {
        'generated_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'total': total,
        'with_readme': with_readme,
        'without_readme': without_readme,
    }
    with open(DEEP / 'generation_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)


if __name__ == '__main__':
    main()

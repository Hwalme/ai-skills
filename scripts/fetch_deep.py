#!/usr/bin/env python3
"""批量抓取 1714 skills 的 README 内容 → deep/readmes/ + enriched_catalog.json"""
import json, os, re, hashlib, time, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE = Path(__file__).parent
DEEP = BASE / "deep"
READMES = DEEP / "readmes"
DEEP.mkdir(parents=True, exist_ok=True)
READMES.mkdir(parents=True, exist_ok=True)

CATALOG = BASE / "catalog-final" / "catalog.json"
OUTPUT = DEEP / "enriched_catalog.json"
PROGRESS = DEEP / "fetch_progress.jsonl"
MAX_WORKERS = 10
TIMEOUT = 12
MAX_CONTENT = 30000  # max chars to keep per README

# 解析 GitHub URL → (owner, repo, branch)
GITHUB_RE = re.compile(r'(?:https?://)?github\.com/([^/]+)/([^/]+?)(?:\.git)?(?:\.[^.]+)?(?:/tree/([^/]+)(?:/.*)?)?(?:/blob/([^/]+)/.*)?$')


def parse_github(url):
    m = GITHUB_RE.match(url.strip('/'))
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3) or m.group(4) or 'main'


def fetch_readme_github(owner, repo):
    """Fetch README.md from raw.githubusercontent.com, try main then master."""
    for branch in ['main', 'master']:
        for readme_name in ['README.md', 'readme.md', 'README', 'Readme.md']:
            url = f'https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{readme_name}'
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                    if resp.status == 200:
                        content = resp.read().decode('utf-8', errors='replace')[:MAX_CONTENT]
                        return content, url, 'ok'
            except Exception:
                continue
    # Try GitHub API as fallback (no token → 60/hr limit, use sparingly)
    try:
        api_url = f'https://api.github.com/repos/{owner}/{repo}/readme'
        req = urllib.request.Request(api_url, headers={
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/vnd.github.v3.raw'
        })
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            if resp.status == 200:
                content = resp.read().decode('utf-8', errors='replace')[:MAX_CONTENT]
                return content, api_url, 'ok'
    except Exception:
        pass
    return '', '', 'no_readme'


def fetch_generic(url):
    """Generic fetch for non-GitHub URLs"""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            if resp.status == 200:
                ct = resp.headers.get('Content-Type', '')
                if 'text/html' in ct:
                    return '', url, 'skip_html'
                content = resp.read().decode('utf-8', errors='replace')
                if content.startswith('<!DOCTYPE') or content.startswith('<html'):
                    return '', url, 'skip_html'
                return content[:MAX_CONTENT], url, 'ok'
    except urllib.error.HTTPError as e:
        return '', url, f'http_{e.code}'
    except Exception as e:
        return '', url, str(e)[:100]


def fetch_one(skill):
    """Fetch README for one skill. Returns dict with _content for file saving."""
    name = skill['n']
    url = skill['u']
    gh = parse_github(url)
    content = ''
    if gh:
        owner, repo, _ = gh
        content, source_url, status = fetch_readme_github(owner, repo)
    else:
        content, source_url, status = fetch_generic(url)

    content_hash = hashlib.sha1(content.encode()).hexdigest() if content else ''
    r = {
        'name': name,
        'url': url,
        'github': bool(gh),
        'owner': gh[0] if gh else '',
        'repo': gh[1] if gh else '',
        'status': status,
        'content_len': len(content),
        'content_hash': content_hash,
        'source_url': source_url,
        '_content': content,
    }
    return r


def main():
    with open(CATALOG, 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    # flatten skills
    skills = []
    def walk(node, keys):
        if not node:
            return
        if node.get('leaf'):
            for it in node.get('items', []):
                skills.append(it)
            return
        for k in node.get('children', {}):
            walk(node['children'][k], keys + [k])
    for b in catalog['boards']:
        walk(b['data'], [b['name']])

    total = len(skills)
    print(f'Total skills: {total}')

    # Load existing progress for resume
    done = {}
    if PROGRESS.exists():
        with open(PROGRESS, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                    done[r['url']] = r
                except:
                    pass
        print(f'Resume: {len(done)} already fetched')

    to_fetch = [s for s in skills if s['u'] not in done]
    print(f'To fetch: {len(to_fetch)}')

    if not to_fetch:
        print('All done!')
        return

    # Fetch in parallel
    done_since = 0
    start = time.time()
    f_out = open(PROGRESS, 'a', encoding='utf-8')

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(fetch_one, s): s for s in to_fetch}
        for future in as_completed(futures):
            skill = futures[future]
            try:
                result = future.result()
            except Exception as e:
                result = {'name': skill['n'], 'url': skill['u'], 'status': f'exception:{e}', 'content_len': 0}

            # Save README content to file
            content = result.pop('_content', '')
            if content:
                hash_name = result['content_hash']
                readme_file = READMES / f'{hash_name}.md'
                readme_file.write_text(content, encoding='utf-8')

            # Write progress (compact, no content)
            line = json.dumps(result, ensure_ascii=False)
            f_out.write(line + '\n')
            f_out.flush()

            done[result['url']] = result
            done_since += 1
            if done_since % 50 == 0:
                elapsed = time.time() - start
                rate = done_since / elapsed
                remaining = (len(to_fetch) - done_since) / rate if rate > 0 else 0
                ok_count = sum(1 for v in list(done.values())[-done_since:] if v['status'] == 'ok')
                print(f'  {done_since}/{len(to_fetch)} | rate {rate:.1f}/s | ok last50: {ok_count}/{min(50,done_since)} | ETA {remaining:.0f}s')

    f_out.close()
    elapsed = time.time() - start
    print(f'\nDone! {len(to_fetch)} fetched in {elapsed:.0f}s ({len(to_fetch)/elapsed:.1f}/s)')

    # Build enriched catalog
    print('Building enriched_catalog.json...')
    enriched = catalog.copy()
    enriched['_fetched_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    enriched['_total_fetched'] = len(done)
    enriched['_ok'] = sum(1 for v in done.values() if v['status'] == 'ok')
    enriched['_no_readme'] = sum(1 for v in done.values() if v['status'] == 'no_readme')
    enriched['_skip_html'] = sum(1 for v in done.values() if v['status'] == 'skip_html')
    enriched['_error'] = sum(1 for v in done.values() if v['status'] not in ('ok', 'no_readme', 'skip_html'))

    def enrich_node(node):
        if not node:
            return
        if node.get('leaf'):
            for it in node.get('items', []):
                r = done.get(it['u'], {})
                it['fetch_status'] = r.get('status', '')
                it['readme_hash'] = r.get('content_hash', '')
                it['readme_len'] = r.get('content_len', 0)
                it['readme_source'] = r.get('source_url', '')
                if r.get('content_len', 0) > 0:
                    fn = r.get('content_hash', hashlib.sha1(it['n'].encode()).hexdigest()) + '.md'
                    it['readme_file'] = f'deep/readmes/{fn}'
            return
        for k in node.get('children', {}):
            enrich_node(node['children'][k])
    for b in enriched['boards']:
        enrich_node(b['data'])

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)
    print(f'Saved {OUTPUT} ({OUTPUT.stat().st_size} bytes)')

    # Summary
    print('\n--- Summary ---')
    print(f'Total: {total}')
    print(f'OK: {enriched["_ok"]}')
    print(f'No README: {enriched["_no_readme"]}')
    print(f'Skipped (HTML): {enriched["_skip_html"]}')
    print(f'Errors: {enriched["_error"]}')


if __name__ == '__main__':
    main()

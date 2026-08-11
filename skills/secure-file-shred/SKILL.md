---
name: secure-file-shred
description: >-
  Use when the user needs to permanently and irrecoverably delete a file or
  directory on local disk — not just remove the directory entry. Covers
  secure overwrite (zero-fill + random pass), fsync, and unlink, with a
  safe fallback. Applies to secure-delete requirements, "shred"/"wipe"
  requests, privacy-sensitive cleanup, and proof that deletion is physical
  not just logical.
license: MIT
compatibility: >-
  Python 3.8+ (cross-platform). Pure standard library; no third-party
  dependencies. Works on Windows, Linux, macOS. Note: on SSD/COW
  filesystems overwrite is best-effort due to wear-leveling — document this
  caveat when claiming physical unrecoverability.
metadata:
  author: hwalme
  version: "1.0"
  tags:
    - security
    - file-operations
    - privacy
    - deletion
---

# Secure File Shred

`fs.unlink` / `os.remove` only deletes the **directory entry** — the bytes
stay on disk and are trivially recoverable with forensic tools. A "secure
delete" claim backed only by `unlink` is **dishonest**. Do it properly.

## When to use
- User asks to "securely delete", "shred", "wipe", "permanently erase".
- Cleaning up sensitive artifacts (keys, temp uploads, orphaned files).
- Any feature that advertises "physical deletion" / "不可恢复删除".

## Procedure
1. **Validate the path.** Reject symlinks-to-/ or paths outside the
   intended scope. Refuse anything under system roots (`/`, `C:\`,
   `/System`, `AppData`) — never shred blindly.
2. **Overwrite, then unlink** (per `scripts/secure_delete.py`):
   - Pass 1 — **zero-fill** in 64 KB blocks until file size is covered.
   - Pass 2 — **random-byte** overwrite (os.urandom) in 64 KB blocks.
   - `os.fsync(f.fileno())` + `os.fsync(dir_fd)` to force flush to disk.
   - `os.remove(path)` (unlink) as the final step.
3. **Directories:** walk leaf-first, shred each file, then rmdir.
4. **Failure policy:** if overwrite throws (e.g. permission), fall back to a
   plain unlink but **log a warning** that the data may be recoverable.
   Never claim "shredded" on fallback.
5. **Verify** by checking the file no longer exists; report bytes-overwritten
   count for auditability.

## Hard rules
- Do NOT use `rm -rf` on personal/user directories — use trash or this
  overwrite flow only within the explicitly intended scope.
- Never silently downgrade to plain unlink without flagging it.
- On SSD/COW, state the wear-leveling caveat: overwrite is best-effort.

## Bundled script
`scripts/secure_delete.py <path> [--dry-run]` — default dry-run prints what
would be shredded; `--execute` performs the real overwrite+unlink.

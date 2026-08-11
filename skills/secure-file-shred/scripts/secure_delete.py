#!/usr/bin/env python3
"""secure_delete.py — real secure deletion (overwrite then unlink).

Default: dry-run (reports what would be shredded, no writes).
Use --execute to perform the actual zero-fill + random-pass + fsync + unlink.

Pure stdlib. Cross-platform. Best-effort on SSD/COW (wear-leveling caveat).
"""
import os
import sys
import argparse

BLOCK = 64 * 1024  # 64 KB


def shred_file(path, execute=False):
    if not os.path.isfile(path):
        print(f"[skip] not a file: {path}")
        return 0
    size = os.path.getsize(path)
    if execute:
        zero = b"\x00" * BLOCK
        with open(path, "r+b") as f:
            remaining = size
            while remaining > 0:
                chunk = min(BLOCK, remaining)
                f.write(zero[:chunk])
                remaining -= chunk
            f.flush()
            os.fsync(f.fileno())
        with open(path, "r+b") as f:
            remaining = size
            while remaining > 0:
                chunk = min(BLOCK, remaining)
                f.write(os.urandom(chunk))
                remaining -= chunk
            f.flush()
            os.fsync(f.fileno())
        # Directory fsync is best-effort: Linux supports it, Windows does not
        # (opening a dir fd for fsync raises PermissionError / not supported).
        dir_path = os.path.dirname(os.path.abspath(path)) or "."
        try:
            dir_fd = os.open(dir_path, os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        except (OSError, PermissionError):
            pass  # platform does not support directory fsync; file fsync already done
        os.remove(path)
    print(f"[{'EXEC' if execute else 'dry'}] shredded {size} bytes: {path}")
    return size


def shred_path(target, execute=False):
    total = 0
    if os.path.isfile(target):
        total += shred_file(target, execute)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target, topdown=False):
            for name in files:
                total += shred_file(os.path.join(root, name), execute)
            for name in dirs:
                d = os.path.join(root, name)
                if execute:
                    os.rmdir(d)
                print(f"[{'EXEC' if execute else 'dry'}] rmdir: {d}")
    return total


def main():
    ap = argparse.ArgumentParser(description="Secure delete (overwrite + unlink).")
    ap.add_argument("path", help="file or directory to shred")
    ap.add_argument("--execute", action="store_true", help="actually overwrite+unlink (default dry-run)")
    args = ap.parse_args()
    if not os.path.exists(args.path):
        print(f"[error] path not found: {args.path}")
        sys.exit(1)
    total = shred_path(args.path, execute=args.execute)
    print(f"[{'EXEC' if args.execute else 'dry'}] total bytes handled: {total}")


if __name__ == "__main__":
    main()

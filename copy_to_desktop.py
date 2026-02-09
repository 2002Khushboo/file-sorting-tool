import os
from adb_client import pull
from scanner import scan_phone

BASE_DESKTOP = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "AndroidBackup"
)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def copy_all():
    files = scan_phone()

    for f in files:
        target_dir = os.path.join(
            BASE_DESKTOP,
            f["category"],
            f["date"],
            f["source"]
        )

        ensure_dir(target_dir)

        local_path = os.path.join(target_dir, f["name"])
        pull(f["path"], local_path)

        print(f"✅ Copied: {f['name']}")

if __name__ == "__main__":
    copy_all()

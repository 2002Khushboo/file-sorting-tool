from PySide6.QtCore import QThread, Signal
from scanner import scan_phone
from adb_client import pull
import os

class BackupWorker(QThread):
    log = Signal(str)
    progress = Signal(int)
    finished = Signal()

    def run(self):
        files = scan_phone()

        total = len(files)
        if total == 0:
            self.log.emit("❌ No files found")
            self.finished.emit()
            return

        base_desktop = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "AndroidBackup"
        )

        for i, f in enumerate(files, start=1):
            target_dir = os.path.join(
                base_desktop,
                f["category"],
                f["date"],
                f["source"]
            )

            os.makedirs(target_dir, exist_ok=True)

            local_path = os.path.join(target_dir, f["name"])
            pull(f["path"], local_path)

            self.log.emit(f"✅ Copied: {f['name']}")
            self.progress.emit(int(i / total * 100))

        self.finished.emit()

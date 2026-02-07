print("MAIN.PY STARTED")

'''
import sys
import os
import shutil
from datetime import datetime

import win32com.client
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTextEdit,
    QVBoxLayout, QWidget, QProgressBar, QMessageBox
)
from PySide6.QtCore import Qt, QThread, Signal


# ---------------- CONFIG ---------------- #

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".webp", ".heic")
VIDEO_EXT = (".mp4", ".mkv", ".mov", ".avi")
AUDIO_EXT = (".mp3", ".aac", ".wav", ".ogg")
DOC_EXT = (".pdf", ".docx", ".xlsx", ".pptx")

SCAN_FOLDERS = [
    "DCIM",
    "Pictures",
    "Movies",
    "Music",
    "Download",
    "WhatsApp",
    "Telegram"
]

DEST_ROOT = os.path.join(os.path.expanduser("~"), "Desktop", "Android Backup")


# ---------------- HELPERS ---------------- #

def classify_file(name):
    lname = name.lower()
    if lname.endswith(IMAGE_EXT):
        return "Images"
    if lname.endswith(VIDEO_EXT):
        return "Videos"
    if lname.endswith(AUDIO_EXT):
        return "Audio"
    if lname.endswith(DOC_EXT):
        return "Documents"
    return None


def detect_source(path):
    p = path.lower()
    if "whatsapp" in p:
        return "WhatsApp"
    if "telegram" in p:
        return "Telegram"
    if "dcim" in p or "camera" in p:
        return "Camera"
    if "screenshot" in p:
        return "Screenshots"
    return "Others"


# ---------------- ANDROID SCANNER ---------------- #

class AndroidScanner(QThread):
    log_signal = Signal(str)
    progress_signal = Signal(int)
    finished_signal = Signal()

    def run(self):
        try:
            shell = win32com.client.Dispatch("Shell.Application")
            this_pc = shell.Namespace(17)  # This PC

            device = None
            for item in this_pc.Items():
                name = item.Name.lower()
                if "phone" in name or "android" in name:
                    device = item
                    break

            if not device:
                self.log_signal.emit("❌ No Android device detected.")
                return

            self.log_signal.emit(f"📱 Device detected: {device.Name}")

            storage = device.GetFolder()
            all_files = []

            for folder in storage.Items():
                if folder.Name in SCAN_FOLDERS:
                    self.log_signal.emit(f"🔍 Scanning {folder.Name}...")
                    self.scan_folder(folder.GetFolder(), all_files)

            total = len(all_files)
            if total == 0:
                self.log_signal.emit("⚠ No files found.")
                return

            self.log_signal.emit(f"📦 Total files found: {total}")
            self.copy_files(all_files)

        except Exception as e:
            self.log_signal.emit(f"🔥 Error: {e}")

        self.finished_signal.emit()

    def scan_folder(self, folder, collected):
        for item in folder.Items():
            if item.IsFolder:
                self.scan_folder(item.GetFolder(), collected)
            else:
                file_type = classify_file(item.Name)
'''
'''
import sys
from PySide6.QtWidgets import QApplication, QWidget

print("Before app")

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("TEST WINDOW")
w.show()

print("Before exec")
sys.exit(app.exec())

'''

import sys
import os
import shutil
from datetime import datetime

import win32com.client
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTextEdit,
    QVBoxLayout, QWidget, QProgressBar, QMessageBox
)
from PySide6.QtCore import QThread, Signal


print("MAIN.PY STARTED")  # sanity check


# ---------------- CONFIG ---------------- #

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".webp", ".heic")
VIDEO_EXT = (".mp4", ".mkv", ".mov", ".avi")
AUDIO_EXT = (".mp3", ".aac", ".wav", ".ogg")
DOC_EXT = (".pdf", ".docx", ".xlsx", ".pptx")

SCAN_FOLDERS = [
    "DCIM",
    "Pictures",
    "Movies",
    "Music",
    "Download",
    "WhatsApp",
    "Telegram"
]

DEST_ROOT = os.path.join(os.path.expanduser("~"), "Desktop", "Android Backup")


# ---------------- HELPERS ---------------- #

def classify_file(name):
    lname = name.lower()
    if lname.endswith(IMAGE_EXT):
        return "Images"
    if lname.endswith(VIDEO_EXT):
        return "Videos"
    if lname.endswith(AUDIO_EXT):
        return "Audio"
    if lname.endswith(DOC_EXT):
        return "Documents"
    return None


def detect_source(path):
    p = path.lower()
    if "whatsapp" in p:
        return "WhatsApp"
    if "telegram" in p:
        return "Telegram"
    if "dcim" in p or "camera" in p:
        return "Camera"
    if "screenshot" in p:
        return "Screenshots"
    return "Others"


# ---------------- WORKER THREAD ---------------- #

class AndroidScanner(QThread):
    log_signal = Signal(str)
    progress_signal = Signal(int)
    finished_signal = Signal()

    def run(self):
        self.log_signal.emit("🚀 Scan started")

        try:
            shell = win32com.client.Dispatch("Shell.Application")
            this_pc = shell.Namespace(17)  # This PC

            self.log_signal.emit("🖥 Scanning devices under This PC:")

            device = None

            for item in this_pc.Items():
                self.log_signal.emit(f"   🔹 Found: {item.Name}")

                name = item.Name.lower()

                # Skip obvious non-devices
                if name.startswith("local disk") or name.startswith("system"):
                    continue

                if name in ["desktop", "documents", "downloads", "pictures", "music", "videos", "3d objects"]:
                    continue

                # This is likely an MTP device (your Y22)
                device = item
                break

            if not device:
                self.log_signal.emit("❌ No Android-like device detected")
                self.finished_signal.emit()
                return

            self.log_signal.emit(f"📱 Selected device: {device.Name}")

            device_root = device.GetFolder()

            internal_storage = None
            for item in device_root.Items():
                self.log_signal.emit(f"📁 Found root item: {item.Name}")
                if "internal" in item.Name.lower():
                    internal_storage = item.GetFolder()
                    break

            if not internal_storage:
                self.log_signal.emit("❌ Internal shared storage not found")
                self.finished_signal.emit()
                return

            self.log_signal.emit("📂 Internal shared storage opened")

            collected_files = []

            for folder in internal_storage.Items():
                if folder.Name in SCAN_FOLDERS:
                    self.log_signal.emit(f"🔍 Scanning {folder.Name} ...")
                    self.scan_folder(folder.GetFolder(), collected_files)

            if not collected_files:
                self.log_signal.emit("⚠ No supported files found")
                self.finished_signal.emit()
                return

            self.log_signal.emit(f"📦 Total files found: {len(collected_files)}")
            self.copy_files(collected_files)

        except Exception as e:
            self.log_signal.emit(f"🔥 Error: {e}")

        self.finished_signal.emit()

    def scan_folder(self, folder, collected):
        for item in folder.Items():
            if item.IsFolder:
                self.scan_folder(item.GetFolder(), collected)
            else:
                if classify_file(item.Name):
                    collected.append(item)

    def copy_files(self, files):
        total = len(files)
        copied = 0

        for item in files:
            try:
                file_type = classify_file(item.Name)
                source = detect_source(item.Path)

                try:
                    dt = datetime.fromtimestamp(item.ModifyDate.timestamp())
                except Exception:
                    dt = datetime.now()

                year = str(dt.year)
                month = dt.strftime("%m-%b")

                dest_dir = os.path.join(
                    DEST_ROOT,
                    file_type,
                    year,
                    month,
                    source
                )

                os.makedirs(dest_dir, exist_ok=True)

                dest_path = os.path.join(dest_dir, item.Name)
                shutil.copy2(item.Path, dest_path)

                copied += 1
                self.progress_signal.emit(int((copied / total) * 100))

            except Exception as e:
                self.log_signal.emit(f"⚠ Failed: {item.Name} ({e})")


# ---------------- UI ---------------- #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Android File Organizer v1")
        self.setMinimumSize(700, 500)

        self.start_btn = QPushButton("Scan & Copy Files")
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.progress = QProgressBar()

        layout = QVBoxLayout()
        layout.addWidget(self.start_btn)
        layout.addWidget(self.progress)
        layout.addWidget(self.log_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.start_btn.clicked.connect(self.start_scan)

    def start_scan(self):
        self.log_box.clear()
        self.progress.setValue(0)

        self.worker = AndroidScanner()
        self.worker.log_signal.connect(self.log_box.append)
        self.worker.progress_signal.connect(self.progress.setValue)
        self.worker.finished_signal.connect(self.scan_done)

        self.start_btn.setEnabled(False)
        self.worker.start()

    def scan_done(self):
        self.start_btn.setEnabled(True)
        QMessageBox.information(self, "Done", "Scan & copy finished!")


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

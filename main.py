
'''
from adb_client import is_device_connected

def start_scan(self):
    if not is_device_connected():
        self.log("❌ No Android device connected")
        return

    self.log("📱 Android device detected")
'''

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QTextEdit, QProgressBar
)
from PySide6.QtCore import Qt
from ui_worker import BackupWorker
from adb_client import is_device_connected

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Android File Organizer (V1)")
        self.setFixedSize(500, 400)

        layout = QVBoxLayout()

        self.start_btn = QPushButton("Start Backup")
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.progress = QProgressBar()

        layout.addWidget(self.start_btn)
        layout.addWidget(self.log_box)
        layout.addWidget(self.progress)

        self.setLayout(layout)

        self.start_btn.clicked.connect(self.start_backup)

    def log(self, text):
        self.log_box.append(text)

    def start_backup(self):
        if not is_device_connected():
            self.log("❌ No Android device connected")
            return

        self.log("📱 Device detected")
        self.start_btn.setEnabled(False)
        self.progress.setValue(0)

        self.worker = BackupWorker()
        self.worker.log.connect(self.log)
        self.worker.progress.connect(self.progress.setValue)
        self.worker.finished.connect(self.backup_finished)

        self.worker.start()

    def backup_finished(self):
        self.log("🎉 Backup completed")
        self.start_btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

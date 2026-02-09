from adb_client import is_device_connected

def start_scan(self):
    if not is_device_connected():
        self.log("❌ No Android device connected")
        return

    self.log("📱 Android device detected")

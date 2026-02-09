from adb_client import is_device_connected, list_dir

if not is_device_connected():
    print("❌ No device")
    exit()

print("✅ Device connected")
print(list_dir("/sdcard"))

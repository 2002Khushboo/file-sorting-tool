import subprocess

def adb(cmd):
    result = subprocess.run(
        ["adb"] + cmd,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def is_device_connected():
    output = adb(["devices"])
    lines = output.splitlines()
    return any("\tdevice" in line for line in lines)

def list_dir(path):
    return adb(["shell", "ls", path]).splitlines()

def pull(remote, local):
    subprocess.run(["adb", "pull", remote, local])

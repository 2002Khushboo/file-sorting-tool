from adb_client import adb
from datetime import datetime
import os

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".webp")
VIDEO_EXT = (".mp4", ".mkv", ".avi")
AUDIO_EXT = (".mp3", ".wav", ".aac")
DOC_EXT   = (".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx")

ALL_EXT = IMAGE_EXT + VIDEO_EXT + AUDIO_EXT + DOC_EXT

'''
SCAN_DIRS = {
    "DCIM/Camera": "Camera",
    "Pictures/WhatsApp Images": "WhatsApp",
    "Pictures/Screenshots": "Screenshots",
    "Video": "Videos",
    "Music": "Music",
    "Download": "Downloads"
}
'''

def classify_file(filename):
    name = filename.lower()
    if name.endswith(IMAGE_EXT):
        return "Images"
    if name.endswith(VIDEO_EXT):
        return "Videos"
    if name.endswith(AUDIO_EXT):
        return "Audio"
    if name.endswith(DOC_EXT):
        return "Documents"
    return None

def list_files(remote_dir):
    output = adb(["shell", "ls", "-1", remote_dir])
    return output.splitlines()

def get_file_date(remote_path):
    stat = adb(["shell", "stat", "-c", "%y", remote_path]).strip()

    if not stat:
        # fallback if stat fails
        return datetime.now().strftime("%Y-%m-%d")

    return stat.split()[0]

'''
def scan_phone():
    results = []

    for folder, source in SCAN_DIRS.items():
        remote_base = f"/sdcard/{folder}"

        files = list_files(remote_base)
        if not files:
            continue
        for file in files:
            category = classify_file(file)
            if not category:
                continue

            full_path = f"{remote_base}/{file}"
            date = get_file_date(full_path)

            results.append({
                "category": category,
                "source": source,
                "date": date,
                "path": full_path,
                "name": file
            })

    return results
'''
def scan_phone():
    results = []

    # Run recursive find
    # output = adb(["shell", "find", "/sdcard", "-type", "f"])
    '''output = adb([
        "shell",
        "find", "/storage/emulated/0",
        "-type", "f",
        #"!", "-path", "/storage/emulated/0/Android/data/*"
        #"-path", "/storage/emulated/0/Android/data/*", "-prune",
        #"-o",        
        #"-print"
    ])'''
    output = adb([
        "shell",
        "find", "/storage/emulated/0",
        "-path", "/storage/emulated/0/Android/data", "-prune",
        "-o",
        "-path", "/storage/emulated/0/Android/obb", "-prune",
        "-o",
        "-type", "f",
        "-print"
    ])

    print("RAW FIND OUTPUT:")
    print(output[:500])

    files = output.splitlines()

    for full_path in files:
        filename = os.path.basename(full_path)
        category = classify_file(filename)

        if not category:
            continue

        date = get_file_date(full_path)

        results.append({
            "category": category,
            "source": "All Storage",
            "date": date,
            "path": full_path,
            "name": filename
        })

    return results
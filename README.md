# Android File Transfer & Organizer (V1)

A Windows desktop tool to scan an Android device via ADB and automatically
organize files (images, videos, audio, documents) into a clean,
date-wise and source-wise folder structure on the desktop.

## Why this exists
Windows Explorer + Android MTP is slow, unreliable, and painful for bulk transfers.
This tool accesses Android storage directly using ADB for speed and correctness.

## Features (V1)
- Detects connected Android device
- Scans common media folders
- Categorizes files:
  - Images
  - Videos
  - Audio
  - Documents
- Organizes by:
  - Date
  - Source (Camera, WhatsApp, Screenshots, etc.)
- Copies files safely to Desktop

## Tech Stack
- Python 3
- ADB (Android Debug Bridge)
- PySide6 (UI)

## Requirements
- Windows
- Android device
- USB Debugging enabled
- ADB installed and added to PATH

## How to run (V1)
```bash
python app/copy_to_desktop.py

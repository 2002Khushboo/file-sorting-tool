# Design Decisions

## Initial Approach: Windows Explorer (MTP)

The first implementation attempted to access the Android device using
Windows Shell APIs (`Shell.Application`) via Python (`win32com`).

### Why this seemed reasonable
- Android devices appear under "This PC" in Windows Explorer
- Manual file browsing works via drag-and-drop
- Avoids USB debugging, improving user experience

### What went wrong
Android devices use MTP (Media Transfer Protocol), which is not a real
mounted file system. Windows Explorer virtualizes folder access.

As a result:
- Shell COM APIs behave inconsistently
- Folder traversal breaks at runtime
- `GetFolder()` returns strings instead of folder objects
- Recursive scanning is unreliable

This limitation is inherent to MTP and not a Python bug.

---

## Final Approach: ADB (Android Debug Bridge)

The project switched to using ADB for direct file system access.

### Why ADB
- Stable, real file system paths (`/sdcard`)
- Reliable metadata access
- Industry-standard tooling
- Scriptable and predictable behavior

USB debugging is required for V1, but this provides a correct and scalable
foundation.

Future versions can remove this requirement via a companion Android app.

# Key Learnings

## 1. MTP is not a file system
Windows Explorer presents MTP devices as folders, but this is a UI abstraction.
Programmatic access via COM APIs is unreliable.

## 2. Correct abstraction layer matters
Accessing Android storage through ADB avoids OS-specific virtualization issues.

## 3. Metadata on Android is inconsistent
File timestamps and metadata are not always available. Defensive coding and
fallback strategies are required.

## 4. Prototypes should prioritize correctness
Using USB debugging in early versions allowed faster validation and iteration.

## 5. Separation of concerns improves clarity
ADB logic, scanning logic, and UI are kept separate for maintainability.

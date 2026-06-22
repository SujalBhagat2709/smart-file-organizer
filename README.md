# Smart File Organizer

## Overview

Automatically organizes files into folders based on their type.

---

## Files

- file_classifier.py
- organizer.py

---

## Run

```bash
python organizer.py
```

---

## Example

Before:

Downloads/

```text
resume.pdf
photo.jpg
movie.mp4
song.mp3
program.py
```

After:

```text
Downloads/

Documents/
    resume.pdf

Images/
    photo.jpg

Videos/
    movie.mp4

Audio/
    song.mp3

Code/
    program.py

organization_report.txt
```

---

## Generated Report

```text
resume.pdf -> Documents

photo.jpg -> Images

movie.mp4 -> Videos

song.mp3 -> Audio

program.py -> Code
```

---

## Future Improvements

- Duplicate Detection
- AI File Naming
- Date-wise Organization
- Extension Learning
- Real-Time Monitoring
# Contact Book (Python Project)

## Description
This is a simple command-line Contact Book application written in Python.

It allows users to:
- Add contacts
- Search for contacts
- Delete contacts
- List all saved contacts

All data is stored using a Python dictionary and saved to a JSON file so contacts are not lost after closing the program.

---

## Features
- Menu-driven interface using a loop
- Dictionary-based contact storage
- Add / Search / Delete / List functionality
- Persistent storage using JSON file (`contacts.json`)
- Automatic loading of saved contacts on startup
- Safe handling if file does not exist

---

## Concepts Used
- Dictionaries (key-value storage)
- Loops (`while True`)
- Conditionals (`if / elif / else`)
- File handling (`open`, `with`)
- JSON module (`json.dump`, `json.load`)
- Error handling (`try / except`)

---

## How to Run
```bash
python contact_book.py
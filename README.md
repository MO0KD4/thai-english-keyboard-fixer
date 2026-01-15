# Thai Keyboard Layout Fixer

A simple Python tool that fixes text typed with the **wrong Thai / English keyboard layout**.

If you accidentally type Thai while your keyboard is set to English (or vice versa), this tool converts it instantly using a hotkey.

---

## Features

- Automatically detects **Thai or English text**
- Converts text to the correct keyboard layout
- Works system-wide
- Simple hotkey: **Ctrl + Alt + T**
- No UI, lightweight, fast

---

## How It Works

1. Select the text you typed with the wrong keyboard layout
2. Press **Ctrl + Alt + T**
3. The text is:
   - Copied
   - Converted (Thai ↔ English)
   - Pasted back automatically

---

## Hotkey

Ctrl + Alt + T

## Requirements

- Python 3.9+
- Windows OS

Python libraries:
- `pynput`
- `pyperclip`

Install dependencies:
```bash
pip install pynput pyperclip

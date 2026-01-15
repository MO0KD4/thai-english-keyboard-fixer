"""
Thai-English Keyboard Layout Fixer
Hotkey: Ctrl + Alt + T
Copies selected text, converts layout, and pastes it back.
"""
import time
import pyperclip
from pynput import keyboard
from pynput.keyboard import Key, Controller


# 1) Keyboard controller

kb = Controller()


# 2) Thai <-> English mappings

thai_to_eng = {
    'ๅ': '1', '+': '!', '๑': '@', '/': '2', '-': '3',
    '๒': '#', 'ภ': '4', '๓': '$', 'ถ': '5', '๔': '%',
    'ุ': '6', 'ู': '^', 'ึ': '7', '฿': '&',
    'ค': '8', '๕': '*', 'ต': '9', '๖': '(',
    'จ': '0', '๗': ')', 'ข': '-', '๘': '_',
    'ช': '=', '๙': '+',

    'ๆ': 'q', '๐': 'Q', 'ไ': 'w', '"': 'W',
    'ำ': 'e', 'ฎ': 'E', 'พ': 'r', 'ฑ': 'R',
    'ะ': 't', 'ธ': 'T', 'ั': 'y', 'ํ': 'Y',
    'ี': 'u', '๊': 'U', 'ร': 'i', 'ณ': 'I',
    'น': 'o', 'ฯ': 'O', 'ย': 'p', 'ญ': 'P',
    'บ': '[', 'ฐ': '{', 'ล': ']', '`': '`',
    'ฃ': '\\', 'ฅ': '`',

    'ฟ': 'a', 'ฤ': 'A', 'ห': 's', 'ฆ': 'S',
    'ก': 'd', 'ฏ': 'D', 'ด': 'f', 'โ': 'F',
    'เ': 'g', 'ฌ': 'G', '้': 'h', '็': 'H',
    '่': 'j', '๋': 'J', 'า': 'k', 'ษ': 'K',
    'ส': 'l', 'ศ': 'L',

    'ว': ';', 'ซ': ':', 'ง': "'", '.': '"',
    'ผ': 'z', '(': 'Z', 'ป': 'x', ')': 'X',
    'แ': 'c', 'ฉ': 'C', 'อ': 'v', 'ฮ': 'V',
     'ิ': 'b', 'ฺ': 'B', 'ื': 'n', '์': 'N',
     'ื': 'n','ท': 'm','ม': ',','ฒ': '<',
    'ใ': '.','ฬ': '>','ฝ': '/','ฦ': '?','?': 'M'

}

eng_to_thai = {v: k for k, v in thai_to_eng.items()}


# 3) Conversion logic

def thai_detector(text):
    for c in text:
        if '\u0E00' <= c <= '\u0E7F':
            return True
    return False

def convert_thai_to_eng(text):
    return ''.join(thai_to_eng.get(c, c) for c in text)

def convert_eng_to_thai(text):
    return ''.join(eng_to_thai.get(c, c) for c in text)

def auto_convert(text):
    if thai_detector(text):
        return convert_thai_to_eng(text)
    else:
        return convert_eng_to_thai(text)
    

# 4) Hotkey action

def on_activate():
    # Release hotkey modifiers FIRST
    kb.release(Key.ctrl)
    kb.release(Key.alt)

    time.sleep(0.1)

    # Copy
    kb.press(Key.ctrl)
    kb.press('c')
    kb.release('c')
    kb.release(Key.ctrl)

    time.sleep(0.2)

    text = pyperclip.paste()
    if not text.strip():
        return

    converted_text = auto_convert(text)
    pyperclip.copy(converted_text)

    time.sleep(0.1)

    # Paste
    kb.press(Key.ctrl)
    kb.press('v')
    kb.release('v')
    kb.release(Key.ctrl)


hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+t'),
    on_activate
)

def for_canonical(f):
    return lambda k: f(l.canonical(k))

with keyboard.Listener(
    on_press=for_canonical(hotkey.press),
    on_release=for_canonical(hotkey.release)
) as l:
    l.join()
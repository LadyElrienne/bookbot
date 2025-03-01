#!/usr/bin/python3

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def get_num_words(filepath):
    num_words = 0
    text = get_book_text(filepath)
    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def get_num_chars(filepath):
    with open(filepath) as f:
        text = f.read()
        all_lower = text.lower()
    num_chars = {}
    for c in all_lower:
        if c.isalpha():
            if c in num_chars:
                num_chars[c] += 1
            else:
                num_chars[c] = 1
    return num_chars

def get_sorted_list(filepath):
    num_chars = get_num_chars(filepath)
    sorted_list = sorted(num_chars.items(), key=lambda x: x[1], reverse=True)
    return sorted_list
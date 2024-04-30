#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))

    words_file_name = input("Введите название файла со служебными словами: ")
    words_file_path = os.path.join(current_directory, words_file_name)

    with open(words_file_path, "r") as fileptr:
        words = fileptr.readlines()

    words = [word.strip() for word in words]
    print(f"Список служебных слов из файла {words_file_name}:")
    print(*words, sep="\n")

    text_file_name = input("Введите название файла с текстом: ")
    text_file_path = os.path.join(current_directory, text_file_name)

    with open(text_file_path, "r") as fileptr:
        text = fileptr.readlines()

    text = [string.strip() for string in text]
    print(f"Список строк из файла {text_file_name}:")
    print(*text, sep="\n")

    for word in words:
        for i, string in enumerate(text):
            s = string
            while (s.lower()).find(word.lower()) != -1:
                start_index = (s.lower()).find(word.lower())
                end_index = start_index + len(word)
                s = s[:start_index] + "*" * len(word) + s[end_index:]
                text[i] = s

    new_text_file_name = input("Введите название нового файла с текстом: ")
    new_text_file_path = os.path.join(current_directory, new_text_file_name)

    with open(new_text_file_path, "w") as fileptr:
        for string in text:
            fileptr.write(string + "\n")

    with open(new_text_file_path, "r") as fileptr:
        strings = fileptr.readlines()

        print("Список строк из нового файла: ")
        for string in strings:
            print(string.strip())

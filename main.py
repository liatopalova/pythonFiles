import os
import re
import sys

TEXT_FILE = "my_text.txt"
TEXT_FILE_NEW = "my_text_new.txt"
with open(TEXT_FILE, "w") as my_file:
    my_file.write("Lorem ipsum dolor sit amet, "
                  "consectetur adipiscing elit, sed do eiusmod tempor"
                  "incididunt ut labore et dolore magna aliqua. "
                  "Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                  "laboris nisi ut aliquip ex ea commodo consequ")

with open(TEXT_FILE_NEW, "w") as my_file:
    my_file.write("")


def get_text(get_file: str) -> str:
    if os.path.exists(get_file):
        with open(get_file, "r") as file:
            content = file.readlines()
            result: str = ""
            for i in range(len(content)):
                result += content[i]
        return result
    raise FileNotFoundError("File not found!")


str_txt = get_text(TEXT_FILE)


def get_words(text_words: str) -> None:
    text_only = re.sub(r'[^\w\s]', "", text_words)
    list_words = text_only.split(" ")
    for word in list_words:
        if len(word) >= 7:
            with open(TEXT_FILE_NEW, "a") as file:
                file.write(word + ' ')


def count_words(some_text: str) -> int:
    words_list = some_text.split(" ")
    count = 0
    for i in range(len(words_list) + 1):
        if i <= len(words_list):
            count += 1
        else:
            raise Exception("Error!")
    return count


try:
    while True:
        print("1. Get words\n2. Count words")
        user_select = int(input("Enter menu item: "))

        match user_select:
            case 1:
                get_words(str_txt)
            case 2:
                print(f"Count of words in text: {count_words(str_txt)}")
            case 3:
                sys.exit()
            case _:
                raise Exception("Incorrect user select!")
except Exception as error:
    print(error)

import os, re

def prompt_file():
    return input("Enter file location\n : ")

def filter_prompt(prompt):
    return prompt.strip()

def scan_header(filtered_path):
    header_start_pos = 0
    with open(filtered_path, encoding="utf-8") as file_opened:
        scan_line = file_opened.readline()
        while (scan_line.startswith('Marker') != True):
            scan_line = file_opened.readline()
        header_start_pos = file_opened.tell()
    return header_start_pos


if __name__ == "__main__":
    scan_header(
    filter_prompt(
        prompt_file()
    )
   )
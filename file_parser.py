from array import array
import os, re

def prompt_file():
    return input("Enter file location\n : ")

def filter_prompt(prompt):
    return prompt.strip()

def scan_header(filtered_path):
    header = {}
    with open(filtered_path, encoding="utf-8") as file_opened:
        scan_line = file_opened.readline()
        while (scan_line.startswith('Marker') != True):
            scan_line = file_opened.readline()
        header = [
            scan_line,
            file_opened.readline(),
            file_opened.readline()
        ]
    return header

def format_header(header):
    for count, value in enumerate(header):
        header[count] = value.split(',')
        
    for count, value in enumerate(header[1]):
        header[0][count]+= f' {value} {header[2][count]}'
    


if __name__ == "__main__":
    format_header(
        scan_header(
            filter_prompt(
                prompt_file()
            )
        )
    )
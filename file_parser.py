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

def count_markers(filtered_path: str) -> int:
    count = 0
    with open(filtered_path, encoding="utf-8") as file_opened:
        if any(map(lambda x: x.startswith('Marker'), file_opened)):
            count+=1     
    return count

def format_header(header):
    if header == [""]: 
        pass
    for count, value in enumerate(header):
        header[count] = value.split(',')
        
    for count, value in enumerate(header[1]):
        header[0][count]+= f' {value} {header[2][count]}' """ """
    


if __name__ == "__main__":
    format_header(
        scan_header(
            filter_prompt(
                prompt_file()
            )
        )
    )
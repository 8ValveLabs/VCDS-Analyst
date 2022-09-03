from array import array
import os, re

def prompt_file():
    return input("Enter file location\n : ")

def filter_prompt(prompt):
    return prompt.strip()

def cut_header(filtered_path):
    header = {}
    with open(filtered_path, encoding="utf-8") as file_opened:
        timestamp = file_opened.readline()
        carinfo = file_opened.readline()
        sensors = None
        marker_found = False
        while (marker_found == False):
            scanline = file_opened.readline()
            if (scanline.startswith("Marker")):
                sensors = scanline, file_opened.readline()
                marker_found = True
    header = {
        'timestamp' : format_timestamp(timestamp),
        'carinfo' : format_carinfo(carinfo),
        'sensors' : format_sensors(sensors)
    }
    return header

def count_markers(filtered_path: str) -> int:
    count = 0
    with open(filtered_path, encoding="utf-8") as file_opened:
        if any(map(lambda x: x.startswith('Marker'), file_opened)):
            count+=1     
    return count

def format_sensors(sensors: dict) -> dict:
    try:
        slice = sensors[0].split(','), sensors[1].split(',')
        sensors_formatted = {}
        for count, value in enumerate(slice[0]):
            if (value):
                sensors_formatted[count] = f'{value} {slice[1][count]}'
        sensors_formatted.popitem()
    except:
        print(f"Error reading file, sensor marker failed to format\n")
        sensors_formatted = None
    finally:
        return sensors_formatted

def format_carinfo(carinfo: dict) -> dict:
    try:
        sliced = carinfo.split(',')
        carinfo = {
            'chassis_code' : sliced[0],
            'platform_code' : sliced[1],
            'ecu_info' : sliced[2]
        }
    except:
        print("Error reading file, second line failed to format.")
    finally:
        return carinfo

def format_timestamp(timestampinfo: dict) -> dict:
    try:
        sliced = timestampinfo.split(',')
        timestamp = {
            'day_name' : sliced[0],
            'day' : sliced[1],
            'month_name' : sliced[2],
            'year' : sliced[3],
            'vcid' : sliced[4],
            'vcds_version' : sliced[5],
            'data_version' : sliced[6].rstrip()
        }
    except:
        print("Error reading file, first line could not be formatted.")
        sliced = None
    finally:
        return timestamp


if __name__ == "__main__":
    print(cut_header(
        filter_prompt(
            prompt_file()
        )
    ))
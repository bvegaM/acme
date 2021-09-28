from typing import List

import os


def read_text_input(source_path:str):
    try:
        full_path = get_full_path(source_path)
        data = []
        with  open(full_path,'r') as file:
            data = file.readlines()
        return [line.rstrip('\n') for line in data]
    except FileNotFoundError:
        print("File not found in: {path} check the file ubication".format(path=source_path))


def get_full_path(source_path:str)->str:
    home_path:str = os.getcwd()
    return os.path.join(home_path,source_path)
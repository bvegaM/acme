import os
from typing import List
from main.model.person import Person

def read_text_input(source_path:str):
    try:
        full_path = get_full_path(source_path)
        data      = []
        with  open(full_path,'r') as file:
            data  = file.readlines()
        return [line.rstrip('\n') for line in data]
    except FileNotFoundError:
        print("File not found in: {path} check the file ubication".format(path=source_path))

def write_text_output(output_path:str,persons:List[Person]):
    try:
        full_path   = get_full_path(output_path)
        output_file = open(full_path,"w")
        for element in persons:
            output_file.write("The amount to pay {name} is: {salary} USD".format(name=element.name,salary=element.salary))
    except FileNotFoundError:
        print("File not found in: {path} check the file ubication".format(path=output_path))


def get_full_path(source_path:str)->str:
    home_path:str = os.getcwd()
    return os.path.join(home_path,source_path)
import argparse

from main.controller import files
from main.utils.util import get_name,get_workweek
from main.model.person import Person

def main(path:str):
    data = files.read_text_input(path)
    for data_person in data:
        person = Person(get_name(data_person),get_workweek(data_person))
        print(person.salary)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('path',
    help='''Employees work data file path.
    If don't pass the path argument use for default data/input.txt path''',
    type=str,default='./data/input.txt',nargs='?')

    args = parser.parse_args()

    main(args.path)
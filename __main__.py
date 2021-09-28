import argparse

from main.controller import files

def main(path:str):
    data = files.read_text_input(path)
    print(data)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('path',
    help='''Employees work data file path''',
    type=str,default='./data/input.txt')

    args = parser.parse_args()

    main(args.path)
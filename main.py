##
## badger maps, 2022
## badger-maps-test
## File description:
## main
##

from src.Parser import Parser

import sys

def main():
    if (len(sys.argv) < 2):
        print("USAGE: python3 ./main.py {filename}")
        exit()
    parser = Parser(sys.argv[1])
    parser.parse_file()
    parser.get_dates()
    parser.print_names()

if __name__ == "__main__":
    main()
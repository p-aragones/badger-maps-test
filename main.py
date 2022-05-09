##
## badger maps, 2022
## badger-maps-test
## File description:
## main
##

from src.Parser import Parser

import sys

def main():
    parser = Parser(sys.argv[1])
    parser.parse_file()
    parser.first_date()

if __name__ == "__main__":
    main()
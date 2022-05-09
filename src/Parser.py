##
## PARSER CLASS, 2022
## badger-maps-test
## File description:
## Parser
##

from src.Person import Person

import csv

class Parser:
    def __init__(self, path):
        self.path = path
        self.people = []

    def parse_file(self):
        with open(self.path, newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                person = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                self.people.append(person)

    def print_names(self):
        for person in self.people:
            print(person.first_name)
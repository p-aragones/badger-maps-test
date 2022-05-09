##
## PARSER CLASS, 2022
## badger-maps-test
## File description:
## Parser
##

from src.Person import Person

import csv
import time

class Parser:
    def __init__(self, path):
        self.path = path
        self.people = []

    def parse_file(self):
        line = 0

        with open(self.path, newline='') as file:
            next(file)
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                person = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], line)
                line += 1
                self.people.append(person)

    def print_names(self):
        for person in self.people:
            print(person.first_name)
    
    def first_date(self):
        try:
            date = time.strptime(self.people[0].date, "%d/%m/%Y")

        except:
            print("invalid date found at line 2")
        for person in self.people:
            try:
                new_date = time.strptime(person.date, "%d/%m/%Y")
                if (new_date < date):
                    date = new_date
                    customer = person
            except:
                print("invalid date at line", person.line + 2, "of file", self.path)
        print("customer with the oldest check in is", customer.first_name, customer.last_name, "at", end=" ")
        print(date.tm_mday, date.tm_mon, date.tm_year, sep="/")

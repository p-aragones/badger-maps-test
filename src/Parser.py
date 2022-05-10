##
## PARSER CLASS, 2022
## badger-maps-test
## File description:
## Parser
##

from src.Person import Person

import csv
import time
import unidecode

class Parser:
    def __init__(self, path):
        self.path = path
        self.people = []

    def parse_file(self):
        line = 0

        with open(self.path, newline='', encoding="utf8") as file:
            next(file)
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if (len(row) < 10):
                    print("not enough fields in line", line)
                    continue
                person = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], line)
                line += 1
                self.people.append(person)

    def print_names(self):
        full_names = []
        for person in self.people:
            if (person.first_name == "" or person.last_name == ""):
                print("empty field at line", person.line)
            else:
                full_name = person.first_name + " " + person.last_name
                full_names.append(full_name)
        print(sorted(full_names, key=unidecode.unidecode))
    
    def get_dates(self):
        try:
            first_date = last_date = time.strptime(self.people[0].date, "%d/%m/%Y")  
        except:
            print("invalid date found at line 2")
        for person in self.people:
            try:
                new_date = time.strptime(person.date, "%d/%m/%Y")
                if (new_date < first_date):
                    first_date = new_date
                    first_customer = person
                if (new_date > last_date):
                    last_date = new_date
                    last_customer = person
            except:
                print("invalid date at line", person.line, "of file", self.path)
        print("customer with the oldest check-in is", first_customer.first_name, first_customer.last_name, "at", end=" ")
        print(first_date.tm_mday, first_date.tm_mon, first_date.tm_year, sep="/")
        print("customer with the latest check-in is", last_customer.first_name, last_customer.last_name, "at", end=" ")
        print(last_date.tm_mday, last_date.tm_mon, last_date.tm_year, sep="/")
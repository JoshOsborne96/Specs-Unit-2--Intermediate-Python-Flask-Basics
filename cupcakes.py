import csv
from pprint import pprint
from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        

    # def add_sprinkles(self, *args):
    #     for sprinkle in args:
    #         self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price
        
class Mini(Cupcake):
    size = "mini"
    
    def __init__(self, name, price, flavor, frosting):
         self.name = name
         self.price = price
         self.flavor = flavor
         self.frosting = frosting
         

    def calculate_price(self, quantity):
        return quantity * self.price

class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price

class Jumbo(Cupcake):
    size = "jumbo"

    def calculate_price(self, quantity):
        return quantity * self.price  



##instances
cupcake_1 = Mini("Birthday Party", 3.99, "vanilla", "funfetti")
cupcake_2 = Mini("Cotton Candy Cup", 2.99, "cotton candy", "vanilla")
cupcake_3 = Regular("Carrot Cake Cup", 1.99, "carrot cake", "vanilla", "vanilla")
cupcake_4 = Regular("Brownie Blast", 4.99, "brownie", "chocolate", "chocolate")
cupcake_5 = Jumbo("Colossal Chocolate", 6.99, "chocolate", "chocolate", "chocolate")
cupcake_6 = Jumbo("French Toast", 5.99, "cinnamon", "vanilla", "cinnamon")

cupcake_menu = [
    cupcake_1,
    cupcake_2,
    cupcake_3,
    cupcake_4,
    cupcake_5,
    cupcake_6
]

def csv_reader(file):

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

def write_new_csv(file, cupcakes):
    with open(file, 'w', newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "frosting": cupcake.frosting})

write_new_csv("sample.csv", cupcake_menu)

def append_csv(file, cupcake):
    with open(file, 'a', newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "frosting": cupcake.frosting})
        


def display_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in display_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None
    

def add_cupcake_dict(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pprint(row)

print(find_cupcake("cupcakes.csv", "French Toast"))
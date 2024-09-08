"""
Luke McElya
M03 Lab
"""

#initialize Vehicle class
class Vehicle:
    def __init__(self, type):
        self.type = type

#initialize Automobile class with inheritance of Vehicle class
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        Vehicle.__init__(self, type) #call init function of vehicle class for vehicle type
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    #create string for car info
    def __str__(self):
        return ("Vehicle type: " + self.type +
                "\nYear: " + self.year +
                "\nMake: " + self.make +
                "\nModel: " + self.model +
                "\nNumber of doors: " + self.doors +
                "\nType of roof: " + self.roof)

if __name__ == "__main__":
    #input
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter number of doors: ")
    roof = input("Enter roof type: ")
    
    #call class functions with user input
    my_car = Automobile("Car", year, make, model, doors, roof)

    #print car info
    print(my_car)
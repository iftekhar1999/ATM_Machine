#For user input value

class Person:

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

        print(f"Name: {self.a}")
        print(f"ID: {self.b}")
        print(f"Amount: {self.c}")

# Take inputs from the user

name = input("Enter your name: ")
id_number = input("Create a four-digit ID: ")
amount = input("Enter Amount: ")

# Create an instance of the Person class
person = Person(name, id_number, amount)

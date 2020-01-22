
#Exercise 1
"""class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_method(self):
        print(self.make, self.model, self.year)

car = Vehicle("Nissan", "Leaf", "2015")
car.print_method()"""


#Exercise 2
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []
        self.greeting_count = 0
    def greet (self, other_person):
        print(f'Hello {other_person}, I am {self.name}!')
        self.greeting_count += 1
    def print_contact_info(self):
        print(self.name, "email is:", self.email)
        print(self.name, "phone number is:", self.phone)
    def add_friend(self, friend):
        self.friend.append(friend.name)
    def num_friends(self):
        print(len(self.friend))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

#sonny.greet("Jordan")
#jordan.greet("Sonny")

#print(sonny.greeting_count)
#print(jordan.greeting_count)

#jordan.add_friend(sonny)
#sonny.add_friend(jordan)

#jordan.num_friends()
#sonny.print_contact_info()


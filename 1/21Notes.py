"""LETTER SUMMARY CODE """

"""word = input("Enter a word >>")
empty_dict = {}
for letters in word:
    if letters not in empty_dict:
        empty_dict[letters] = 0
empty_dict[letters] += 1
print(empty_dict)"""

#2. Summarize each word count into a dictionary would use the above code
# instead we have to use the .split() method in the input sentence before 
# the for loop

"""CLASSES"""
"""class Greeting:
    def say_hello(self):
        print('hello')"""

#Creating a new object inside a class
"""newGreetingObj = Greeting()"""

#adding a method to the new obj
"""newGreetingObj.say_hello()"""

"""class Student:
    def __init__(self):
        print('constructor called')
    def greeting(self):
        print('Good Morning ')"""

#self is a reference so it points back ot the method

"""aline = Student()
aline.greeting()

alex=Student()
alex.greeting()

shaun=Student()
shaun.greeting()"""

"""class Animal:
    def __init__ (self, name):"""
        #instance variable = self.name = name

"""dog = Animal("dog")
cat = Animal("cat")
horse = Animal("horse")"""
#.name will help call the variable inside the variable in the new object
"""print(dog.name)
print(cat.name)
print(horse.name)"""

#adding more variables to the constrcutor
"""class Student:
    def __init__ (self, name, lname):
        self.name = name
        self.lname = lname
        print(f'{self.name} {self.lname}')
aline = Student("Aline", "Belova")
sean = Student("Sean", "Smith")"""
#one way to print both name and lname in print() - 2nd version is within the def method
"""print(sean.name, sean.lname)
print(aline.name, sean.lname)"""


#import datetime #gives access to curent time
#adding multiple variables to the first constructor - including built in functionc with python
"""class Person:
    def __init__(self, fname, lname, birthdate, address, email):
        self.fname = fname
        self.lname= lname
        self.birthdate = birthdate
        self.address = address
        self.email = email
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day): #self.birthdate is accessing its information
            age -= 1
        return age
        

sammy = Person("Sammy", "Kry", datetime.date(1998, 8, 21), "123 Sesame St", "samme@gmail.com")
print(sammy.fname, sammy.lname)
age = sammy.age()
print(age)"""


"""def greeting(name):
    count = 0
    print(f'Hello {name}')
    count +=1
    print(count)
greeting("daniela")
greeting("alex")
greeting("sam")"""

#adding increments to classes and methods
"""class Person:
    def __init__(self, name):
        self.name = name
        self.count = 0
    def greeting(self):
        print(f'Hello {self.name}')
        self.count += 1
    def printCount(self):
        print(self.count)

aline = Person("aline")
aline.greeting()
aline.greeting()
aline.greeting()
aline.greeting()

aline.printCount()"""
#in class exercise - two people greet each other and print their info
"""class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def greet (self, other_person):
        print(f'Hello {other_person}, I am {self.name}!')
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")"""

#sonny.greet(jordan) # works with print("Hello {}, I am {}!" .format(other_person.name, self.name))

"""sonny.greet("Jordan")
jordan.greet("Sonny")

print(sonny.name, sonny.email, sonny.phone)
print(f'{sonny.email} {sonny.phone}')"""

#private functions (double underscores is super private and one equals semiprivate)

"""class Person:
    def __init__ (self, name):
        self.name = name
        self.count = 0
    def greet (self):
        self._greet()
    def _greet (self):
        self.count += 1
        if self.count > 1:
            print("Stop being so nice")
            self.__reset_count()
        else:
            print("Hello", self.name)
    def __reset_count(self):
        self.count = 0

alex = Person("Alex")
alex.greet()
alex.greet()"""

#created a reverse function type str using class methods
"""class VString(str):
    def reverse(self, name):
        rstring = ""

        for char in name:
            rstring = char + rstring
        return rstring
myString = VString("Hello")
print(myString.capitalize())

reversed = myString.reverse("Hello")
print(reversed)"""


#class Child has to run its objeccts first and runs the parent class next by inheriting
#an altered method is used to grab a method inside its base class
"""class Parent(object):
    def implicit(self):
        print("PARENT implicit()")
    def override(self):
            print("PARENT override()")
    def altered(self):
            print("PARENT altered()")
class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()

son = Child()
son.altered()"""
# if two init exits in both parent and child class then the child class will close first and will not acquire anyhting from its parent class
#unless you add the super method
"""class Character:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
class Hero(Character):
    def __init__(self, weapon, name, power, health):
        self.weapon = weapon
        super(Hero, self).__init__(name, power, health)

aline = Hero("pink gun", "aline", 3, 10)
print """

"""Loop Review"""

#count = 0 
#while count < 3:
  #  print ("Hello!", end=" ")
   # count += 1
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#index = 0
#for index in range(5, 10, 2):
    #print (alphabet[index], end=" ")
    #index += 1
#index = 0
#students = ["Matt", "Foorken", "Alex", "May"]
#students.append("Susan")
#print (students)

"""for outerr_variable in sequence: (range set to 3)
        for inner_variable in sequence: (range set to 3)
        Inner variable must be completed before OuterVaribale can be completed"""



#weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
#days = ["  Monday", "  Tuesday", "  Wednesday", "  Thursday", "  Friday"]
#classL = ["     -Lecture", "     -HW", "     -Solutions"]
#for count in weeks:
 #   print(count)
  #  for count in days:
   #     print(f"{count}")
    #    for count in classL:
     #       print(count)


"""EXAMPLE CODE FOR LESSON PLAN
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
subj = ["Objectives", "Lessons", "Training"]
for outer_var in range(1,6):
    print("Week", outer_var)
    for inner_var in days:
        print(f"\t{inner_var}")
        for lesson in subj:
            print(f"\t\t* {lesson}")"""

"""FUNCTIONS NOTES"""
""" def anyName(parameters(s)):
            body"""

"""myVar = 1
myVar2 = 2
def greeting():
    print("hello world!")
if (myVar==1):
    print('Hello')
greeting()"""


"""def students():
    print("Shu Pei")
    print("Thomas")
    print("Gustavo")
    print("Alim")

print("Day 1: Students in SRE class")
print("lecture: git 101")
students()
print("Day 2: Students in SRE class")
print("lecture: git 102")
students()
print("Day 3: Students in SRE class")
print("lecture: python 101")
students()"""

"""def myFunction():
    for i in range(10):
        print(i)"""

"""def greeting():
    print('Hello')

for i in range(10):
    greeting()"""


"""def seperateRuns():
    print("**************")
    
def getGroceries():
    print('milk')
    print('flour')
    print('sugar')
    print('butter')

    seperateRuns()
for i in range(3):
    getGroceries()"""
 
#def FUNCTION
#def funcName(parameter1, parameter2)
    #body of code
#funcName (argue1, argue2)

"""def greeting(person):
    print(f'Hello {person}')
greeting("Kazim")"""

"""def add(num1, num2):
    print(num1 + num2)
add(4 ,5)"""

"""def concat_list(list1, list2):
    concat = list1 + list2
    return concat
c_result = concat_list([1, 4, 6], [7, 9, 0])
print(c_result)"""

"""def blend(setting, nMinutes):
    desiredSett = 'medium'
    numberofM = 8
    blend(desiredSett, numberofM)
blend('high', 10)
blend('medium', 1)
blend('low', 1)
blend()"""

"""DOES NOT WORK def cal_Avg(input):
    sum = 0
    for num in (input):
        sum += num 
        avg = sum / len(input)
        return avg    
listN = [1, 2, 3, 4, 5, 6]
print(cal_Avg(listN))"""

"""def myFunction(num1, num2, num3):

    return num1*2, num2*3, num3*4
result = myFunction(4, 7, 9)
print(result)
one, two, three = myFunction(4, 7, 9)
print (one)
print(two)
print (three)"""

"""print("Hello")
def greeting(name):
    print(f'hello {name}')
students = ['Kazim', 'Matt', 'Alina', 'Mary', 'Alex']
for name in students:
    greeting (name)
print ("Bye")"""

"""TAX_RATE = .09  # 9 percent tax
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00
def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost
total1 = calculateCost(4, 8)  #  4 small and 8 large widgets
print('Total for first order is', total1)
total2 = calculateCost(12, 15)"""

"""def dance(kind="silly"):
    print("I am doing a %s dance" % kind)
dance("funky") # Totally OK.
 # Error!"""
def myFunction():
    someVariable = 5
someVariable = 10
myFunction()
print(someVariable)
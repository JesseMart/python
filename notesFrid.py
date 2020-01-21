"""HW REVIEW FOR THURSDAY"""
#LOGIC CODE FOR FINDING SMALLEST/LARGEST NUMBER IN A LIST
#CHANGE GREATER THAN SYMBOL
"""def large(x):
    y = x[0]
    for i in x:
        if i > y:
            y = i
    return(y)
print(large( [2,3,4,55, 1,6]))"""
#dictionaries

#import pickle #saving 

my_dictionary = {
    "hello" : "world",
    "square_of_2" : 4,
    0 : 1
}
#data is where the name of the file while go
#fh is the name of the file handler
"""my_dictionary = ["last"]
with open('data.pickle', 'wb') as fh:
    pickle.dump(my_dictionary, fh)"""


"""print(my_dictionary["hello"])
print(my_dictionary.get[4])""" #this function returns a key if its exits, will reutnr "none" if thers is no key

#use for loop to get key and value - .values() does the same
value_list = my_dictionary.values()
for val in value_list:
    print (f'{val} : my_dictionary(value_list)')

"""key_list = my_dictionary.keys()
 for key in keys:
        print(f'{key} : mydictionary(key_list))"""

#checks to see if the key is in the dictionary
"""isItThere = "world" in my_dictionary     
print(isItThere)"""

#replaces value of a key
"""print(my_dictionary)
my_dictionary["hello"] = "greeting"
print(my_dictionary)"""

#keys() gets all the keysin the dictionary - vice versa for values()
"""keys = my_dictionary.keys()
print(keys)"""

#del() deletes a key and its value from the dictionary - the key name is the only valid input
"""del my_dictionary["world"]
print(my_dictionary)"""

#itmes() alternate way to get entries - prints the dictionary as a list of tuples ( , )
"""items = my_dictionary.items()
print(items)"""

#Iterating - prints both key and value in the dictionary in a repeating process
"""for key, value in my_dictionary.items():
    print(f'{key} : {value}')"""
    #print(key)
    #print(value)

#Nesting - you can have an array of dictionaries - 
"""contacts = [{
    "first_name" : "Jesse",
    "last_name" : "Martinez",
    "phone" : {
        "cell" : "333-333-3333", #you can also add a dictionary in a value as part of nesting 
        "home" : "444-444-4444"
    }
    }, 
    {
        "first_name" : "Matt",
        "last_name" : "Martinez"
    }, 
    {
        "first_name" : "Matt",
        "last_name" : "Martinez" 
    }]"""
"""print(contacts[0]) """ #works the same way as calling any value in an array - prints out the whole array
"""print(contacts[0]["first_name"])""" # accessing specific dictionary and key
"""print (contacts[0]["first_name"], contacts[0]["last_name"])""" # prints out specific values without braces or quotations
"""print(contacts[0]["phone"]["cell"])""" # prints nested dictionary values

"""print(my_dictionary)"""
"""my_dictionary["name"] = "Jose" """#adds a new key and value to dictionary
"""print(my_dictionary)"""
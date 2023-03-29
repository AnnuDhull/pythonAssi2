# acessing elements from a set.............

cars = {"BMW","Audi","Jaguar","Fortuner", "Range Rover","Rolls Royce","Ferrari","Lamborghini" ,"Bugatti"}
print("Jaguar" in cars)
print("Verna" in cars)

# OUTPUT : True     False

# ---------------------------------------------------------------------------------------------------------------------------

#  D/B remove and discard function ...............

#  ---discard () method removes the specified item from the set. 
# --- using discard() function

cars = {"BMW","Audi","Jaguar","Fortuner", "Range Rover","Rolls Royce","Ferrari","Lamborghini" ,"Bugatti"}
cars.discard("BMW")
cars.discard("verna")
print(cars)

#  OUTPUT : {'Fortuner', 'Lamborghini', 'Audi', 'Jaguar', 'Bugatti', 'Rolls Royce', 'Ferrari', 'Range Rover'}

#                       ----------------------------------------------------------------------------------

# ----if we use remove() function to remove an element from a set that does not exist, then remove() function will raise KeyError
# --- using remove() function

cars = {"BMW","Audi","Jaguar","Fortuner", "Range Rover","Rolls Royce","Ferrari","Lamborghini" ,"Bugatti"}
cars.remove("Audi")
cars.remove("verna")
print(cars)

# OUTPUT : {'Lamborghini', 'Bugatti', 'Fortuner', 'Rolls Royce', 'BMW', 'Jaguar', 'Ferrari', 'Range Rover'}
#          Traceback (most recent call last):
#         File "c:\Users\Annu Dhull\Desktop\annupython\pythonassi2cloudEQ.py", line 29, in <module
#         cars.remove("verna")
#          KeyError: 'verna'

# ------------------------------------------------------------------------------------------------------------------------------

# what is intersection_update().............
#    The intersection_update () method removes the items that is not present in both sets or we can say that it only gives the common elements output.
 
set1 = {23,45,667,87,457,"apple","mango"}
set2 = {56,"apple",66 ,23,45,"cherry",345,467,12}

set1.intersection_update(set2)
print(set1)

# OUTPUT: {'apple', 45, 23}

# -------------------------------------------------------------------------------------------------------------------------------

#  symmetric_difference_update()....................................
#  The symmetric_difference_update() method returns the set with items that are unique in both sets i.e. it removes similar items

set1 = {23,45,667,87,457,"apple","mango"}
set2 = {56,"apple",66 ,23,45,"cherry",345,467,12}
set1.symmetric_difference_update(set2)
print(set1)

# OUTPUT: {66, 457, 'cherry', 12, 467, 87, 345, 667, 'mango', 56}

# -------------------------------------------------------------------------------------------------------------------------------

# symmetric_difference()....................................
# it is a built-in Python set method that returns a new set object with the symmetric difference of two sets.

set1 = {23,45,667,87,457,"apple","mango"}
set2 = {56,"apple",66 ,23,45,"cherry",345,467,12}

set=set1.symmetric_difference(set2)
print(set)

# OUTPUT :{66, 457, 12, 'mango', 467, 'cherry', 87, 56, 345, 667}

# ----------------------------------------------------------------------------------------------------------------------------

# what is dict()..........................
# The dict() function creates a dictionary

myDict = { "Name":"Annu Dhull",
    "Mother Name":"Sunita" ,
    "age":22 ,
    "Siblings":["komal","dhruv"] ,
    "Father Name" : "Daya singh Dhull" , 
    "profession":"Software Engineer"
    }

print(myDict.values())
print(myDict["age"])
myDict.update({"cousin" : "yana"})
print(myDict)

# OUTPUT : dict_values(['Annu Dhull', 'Sunita', 22, ['komal', 'dhruv'], 'Daya singh Dhull', 'Software Engineer'])
#           22
#          {'Name': 'Annu Dhull', 'Mother Name': 'Sunita', 'age': 22, 'Siblings': ['komal', 'dhruv'], 'Father Name': 'Daya singh Dhull', 'profession': 'Software Engineer', 'cousin': 'yana'}

# -----------------------------------------------------------------------------------------------------------------------------------

# using append() function  by converting tuples into a list 

tup1 = ("Annu",34,"grapes",89,76)
lis=list(tup1)
lis.append("Cherry")
print(lis)

# OUTPUT : ['Annu', 34, 'grapes', 89, 76, 'Cherry']

# --------------------------------------------------------------------------------------------------------------------------------
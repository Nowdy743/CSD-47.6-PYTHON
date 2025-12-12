#commenting is important for code readability and maintenance
# There are two types of comments in python : single-line comment and
# multi-line comment.
#single-line comment start with the harsh character(#) and
#extend to the end of the line.
#multi-line comment can be created using trip (''' or""").

#Variables in python
''' variables are used to store data in python.
They are created when you assign a value to a name.
Variables can be of different types,
such as integers,floats,strings,and booleans.
Variable are case-sensitive,
so myVar and myvar are considered variables.

There are rules for naming variables in Python. These includes :
1.1. Variable names must start with a letter 
or the underscore character.
2. Variable names cannot start with a number.
3. Variable names can only contain alpha-numeric characters 
and underscores (A-z, 0-9, and _ ).
4. Variable names are case-sensitive 
(age, Age and AGE are three different variables).
5. Variable names cannot be any of the Python keywords.'''

#Variable Assignment
x =5
#print(x) #to see the outut of variable x, we use the print() funtion.
#check the type of variable. we use the type()function
#print(type(x))

#print(type(x))

#_firstname_ ="Awurabena" # string variable
#print(_firstname_)
#print(type(_firstname_))

#abc_123=12.5 #float variable
#print(abc_123)
#print(type(abc_123))

#2+3J ="Complex" #complex variable
#print(2+3j)

#ABC_123 =3+2j # boleen variable
#print(ABC_123)
#print(type(ABC_123))

#Lists in Python: Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets: [].
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0],
# the second item has index [1] etc.

# When we say that lists are ordered, it means that the items have a defined order,
# and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# The list is changeable, meaning that we can change, add,
# and remove items in a list after it has been created."""

# Since lists are indexed, lists can have items with the same value.
# To determine how many items a list has, use the len() function.
# To add an item to the end of the list, use the append() method.
# To add an item at the specified index, use the insert() method.
# To remove an item from the list, use the remove() method.
# To remove an item at the specified index, use the pop() method.
# To remove all items from the list, use the clear() method.


#healthy_fruits = ["Guava", "Mango", "Pineapple", "Grapes", "Tomatoes", "Avocado"]
#print the list
# print(healthy_fruits)
# print(len(healthy_fruits))  # to check the length of the list
# print(type(healthy_fruits))  # to check the type of the list


#List in another List 
#healthy_vegetables = ["Carrot", "Cabbage", "Spinach", "Onion", "Garlic"]
#healthy_food = [healthy_fruits, healthy_vegetables]
#print(healthy_food)
# print(len(healthy_food))  # to check the length of the list
# print(type(healthy_food))  # to check the type of the list
#print(healthy_food[-2])


#Accessing List Items
#List items are indexed and you can access them by referring to the index number.
#Remember that the first item has index 0.
#print(healthy_fruits[0])  # Access the first item
#print(healthy_fruits[2])  # Access the third item
# print(healthy_fruits[-1]) # Access the last item
# print(healthy_vegetables[-1])
# print(healthy_fruits[-3]) # Access the third last item


#Slicing lists
#You can return a range of items by specifying where to start and where to end the slice
#cars =["Toyota","Honda","Ford","BMW","Audi","Chevrolet","Nissan"]
#print(cars)
#print(cars[0:4])
#print(cars[-4:-1])
#print(cars[2:])
#print(cars[:-3])

#Modify list Items
#You can change the value of a specific item by referring to its index number.
#cars[5] ="Mercedes Benz"
#print(cars)

# How to add items to the end of a list
#cars.append("G wagon")
#print(cars)

#How to add items to a specific index in a list
#cars.insert(1, "Lexus")
#print(cars)

#How to remove items from a list
#cars.remove("Nissan")
#print(cars)

#How to remove an item at a specific index
#cars.pop(2)
#print(cars)

#How to remove an entire list
# del cars
# print(cars)

#How to clear a list
# cars.clear()
# print(cars)

#Tuples in python :Tuples are used to store multiple items in a single variable
#Tuples are one of 4 built-in data types in python used to store collections of 
#data, the other 3 are Lists,Sets,and Dictionary, all with different qualities and 
#usage.Tuples arev written with round brackets()
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0],
#the second item has index [1] etc.
#When we say that tuples are ordered, it means that the items have a defined order,
#and that order will not change.
#If you add new items to a tuple, the new items will be placed at the end of the tuple.
#The tuple is unchangeable, meaning that we cannot change,
#add, or remove items in a tuple after it has been created."""

#Sneakers =("Nike","Addidas","Puma","Reebok","Vans","Converse")
#print the tuple
#print(Sneakers)
# print(len(sneakers))  # to check the length of the tuple
# print(type(sneakers))  # to check the type of the tuple

# #Accessing Tuple Items
# print(sneakers[0])  # Access the first item
# print(sneakers[-5])

#Slicing Tuples
#print(Sneakers[0:3])
#print(Sneakers[-4:-1])

#Modify Tuples
#Tuples are unchangeable,meaning that you cannot change,
#add,remove items once the tuple is creaed
#However, you can convert the tuple into a list, make changes, and convert it back.
# sneakers["Nike"] = "New Balance"
# print(sneakers)

#Convert the tuple into a list to be able to change it:
#sneakers = list(Sneakers)
# print(sneakers)
# sneakers[5] = "New Balance"
# print(sneakers)
# sneakers = tuple(sneakers)
# print(sneakers)
# print(type(sneakers))


#TRY WORK


#list called playlist
#playlist =["Lovely","Halo","Buga","Wash","Cough"]
#print(playlist)

# Tuple Top_artists
# Top_artists =("Beyonce","Shatta Wale","Kizz Daniel","Billie Ellish")
# print(Top_artists)

# new list My_music
# My_music = [playlist,Top_artists]
# print(My_music)

# print how many items are in My_Music should be 2
# print("Total items in My_Music",len(My_music))

#print Third song from playlist
# print("Third song:", playlist[2])

 #  Change the first song in playlist to "Perfect"
# playlist[0] = "Perfect"

#Add the song "Blinding Lights" to the end of playlist
# playlist.append("Blinding Lights")

#Print the complete updated playlist
# print("Updated playlist:", playlist)


#Sets in Python: Sets are used to store multiple items in a single variable.
#Sets are written with curly brackets. {}
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Set items can appear in a different order every time you use them,
#and cannot be referred to by index or key.
#Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Sets cannot have two items with the same value.
#Sets can be any data type, string, integer and boolean.
#Sets are defined as objects with the data type 'set':
#<class 'set'>
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.
#Sets cannot have two items with the same value.
#Sets can be any data type, string, integer and boolean.
#Sets are defined as objects with the data type 'set':


#creating a set.
#Political_parties ={"NDC","NPP","CPP","PPP","GCPP"}
#Print the set
# print(Political_parties)
# print(type(Political_parties))
# print(len(Political_parties))

#Accessing set items. Note Indexing has n0 meaning in sets datatype.
#print (political_parties [0]) # this will raise an error 

#Adding items to the list
# Political_parties.add("New Force")
# print(Political_parties)


#Modifying items in a list 








# student_id = set() # creating an empty set

# student_id_input = int(input("Enter your student ID"))
# student_id.add(student_id_input)
# print("Your student ID has been added.Thank You!", student_id)

#Dictionaries in Python
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, 
#changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have
# keys and values:
#Dictionary items are ordered, changeable, and does not
# allow duplicates.
#Dictionary items are presented in key:value pairs, and 
#can be referred to by using the key name.
#Dictionaries are changeable, meaning that we can change,
# add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key:
#Dictionaries can be of any data type:


#Creating a dictionary
# Student_profile ={
#     "name":'Nana',
#     "complexion":'Fair',
#     "Age":'12'
# }

#print(Student_profile)
#print(type(Student_profile))


#Accessing items in a dictionary
# print(Student_profile["complexion"])

#Modifying items in a dictionary
# Student_profile['Age']= 20
# print(Student_profile)



#Adding items in a dictionary
#Student_profile["Gender"]='Male'
#print(Student_profile)

#Removing items from a dictionary
#Student_profile.pop("complexion")
#print(Student_profile)

#student_profile.clear()
#print(Student_profile)

#del student_profile


#OPERATORS IN PYTHON
#Arithmetic Operators
#Assignment Operators
#Comparison Operators
#Logical Operators
#Identity Operators
#Membership Operators
#Bitwise Operators

#Arithmetic Operators
# +, -, *, /, %, **, //
# print(10 + 20)
# print(10 - 20)
# print(10 * 20)
# print(10 / 20)
# print(10 % 20)
# print(10 ** 20)
# print(10 // 20)

#Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=
# x = 10
# x += 10
# print(x)

#Comparison Operators
# ==, !=, >, <, >=, <=
# print(10 == 10)
# print(10 != 10)
# print(10 > 10)
# print(10 < 10)
# print(10 >= 10)
# print(10 <= 10)

#Logical Operators
# and, or
# print(10 > 5 and 5 < 10)
# print(10 > 5 or 5 > 10)
# print(not(10 > 5))
#Identity Operators
# is, is not
# x = ["apple", "banana"]
# y = x
# print(x is y)
# print(x is not y)
#Membership Operators
# in, not in
# fruits = ["apple", "banana", "cherry"]
# print("banana" in fruits)
# print("orange" not in fruits)
#Bitwise Operators
# &, |, ^, ~, <<, >>
# print(10 & 20)
# print(10 | 20)
# print(10 ^ 20)
# print(~10)
# print(10 << 20)
# print(10 >> 20)


# a = 7
# b = 2

# # addition
# print ('Sum: ', a + b)  

# # subtraction
# print ('Subtraction: ', a - b)   

# # multiplication
# print ('Multiplication: ', a * b)  

# # division
# print ('Division: ', a / b) 

# # floor division
# print ('Floor Division: ', a // b)

# # modulo
# print ('Modulo: ', a % b)  

# # a to the power b
# print ('Power: ',a * * b)
       



# assign 10 to a
# a = 10

# # assign 5 to b
# b = 5 

# # assign the sum of a and b to a
# a += b      # a = a + b

# print(a)


# a = 5

# b = 2

# # equal to operator
# print('a == b =', a == b)

# # not equal to operator
# print('a != b =', a != b)

# # greater than operator
# print('a > b =', a > b)

# # less than operator
# print('a < b =', a < b)

# # greater than or equal to operator
# print('a >= b =', a >= b)

# # less than or equal to operator
# print('a <= b =', a <= b)

#conditional statement in python
# if, elif, else statements
# The if statement used to test a specific condition. 
# If the condition is true, a block of code (if-block) is executed.
#If the condition is false, the if-block is skipped. 

#The syntax of an if statement is:
# if condition:
#     #block of code to be executed if the condition is true


# If statement to ask user to enter a age of a person 
# who is eligible to vote

#Else statement is used to execut a block of code
#  when the condition is false.


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to cast your vote.")
# elif age < 18 and age > 16 :
#     print("You are eligible to cast your vote soon") 
# else:
#     print("You are not eligible to cast your vote.")   



#Example of elif statement 
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("You got A+ grade.")
# elif marks >= 80:
#     print("You got A grade.")
# elif marks >= 70:
#     print("You got B+ grade.")
# elif marks >= 60:
#     print("You got B grade.")
# elif marks >= 50:   
#     print("You got C grade.")
# else:
#     print("You failed the exam. Better luck next time.")



# TRY WORK
age = int(input("Enter your age: "))
if age >= 18 :
  print("You can watch any movie (including Adult-rated)")
elif age >= 13:
   print("You can watch PG-13 and lower-rated movies")
elif age >= 7 :
   print("You can watch G and PG rated movies")
else :
   print("You should watch only G-rated (General Audience) movies")


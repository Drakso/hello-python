# # Variables
# # = -> assignment
# number = 25  # number
# name = "Matej"  # string
# last = 'Trojacanec'  # string
# isM = True  # boolean
# P_rDeZ = "prt prt"  # shitty naming not by convention. Don't do this
# a, b, c = 2, 4, 3  # assign multiple values to multiple variables at the same time
# z = x = v = 2  # assigning all variables at the same time
#
# number = 3  # Until line 7, the value of number variable is 25, from line 8 it is 3
#
# # The console
# # print("Some thing") -> function that prints stuff in the console
# print("Zdr. Asl. Pls.")  # Printing some text
# print("Mace imam kuka stance dojdi na romance")
# print(32)  # Printing some number
# print(name)  # Printing some variable value
#
# # input("Text before input: ") -> gives a chance to the user to input something to the program
# something = input("Write something: ")  # Whatever the person writes, is saved in the "something" variable
# print(something)  # using whatever the user gave us to do some stuff with it ( In our case, just print it )
# input_name = input("What is your name? ")
# input_quest = input("What is your quest? ")
# input_fav_color = input("What is your favorite color? ")
#
# print("--------------------")
# print("The knight name is:")
# print(input_name)
# print("His quest is:")
# print(input_quest)
# print("His favorite color is:")
# print(input_fav_color)
# print("--------------------")
# print("He will surely die.")
#
# # Operations
# sum_of_two = 2 + 5  # We sum two numbers
# sum_of_multiple = sum_of_two - 1  # We get the result of the first sum and subtract 1
# print(sum_of_multiple)
#
# kvadratcho = 2**3  # 2 to the power of 3
# korencho = 9//2  # division but rounded to the lowest number
# modulus = 9 % 2  # division but it returns the left out part of the division
#
# print(kvadratcho)
# print(korencho)
# print(modulus)
#
# # Logic operations
#
# five_is_larger = 5 > 1  # finds out if the statement is true or false and adds the boolean value in the variable
# numbers_are_equal = 3 == 3  # since we are using = for assignment, for equals we use ==
# ten_is_smaller = 10 <= 23  # finds if the number is lower or equal and adds the boolean value in the variable
#
# five_is_larger_than_two_numbers = 5 > 2 and 5 > 1  # if both of them are true, then it is true
# one_is_either_larger_or_smaller = 1 > 5 or 1 < 55  # if none of them is true then it is false
#
# five_not_larger = not five_is_larger
#
# print(five_is_larger)
# print(numbers_are_equal)
# print(ten_is_smaller)
# print(five_is_larger_than_two_numbers)
# print(one_is_either_larger_or_smaller)
# print(five_not_larger)
#
# # Strings
# name = "Matej"
# last = "Trojacanec"
# full_name = name + " " + last  # We can connect two strings with +
# another_full_name = f"{name} {last} is built differently than the previously named: {full_name}"  # another way
# # Bonus: Connection of strings in programming is called concatenation
# broken_full_name = name + last  # If we don't leave empty space it will connect the words
# legit_statement = " e glup"
# another_legit_statement = 'Matej is "Smart"'  # We use '' quotes to have "" quotes in a string and vice versa
# weird_stuff = "ova e navodnik - \" a ova e drug navodnik - ' "
# # If we want treat a character as text we use \ before it ( \ is called escape character )
#
# print(full_name)
# print(broken_full_name)
# print(full_name + legit_statement)
# print(another_legit_statement)
# print(another_full_name)
#
# # We can treat strings as array of characters
# print(len(full_name))  # len(my_string) is a function that returns how many characters are in a string
# print(full_name[0])  # We can get any character from a string by its index ( in our case index 0 or the first letter )
# print(full_name.lower())
# print(full_name.upper())
# print(full_name.split("a"))
# # Bonus: If you write a string or a variable and write . next to it, it will give you all possible methods to that
#
# # If
# name = input("Enter your name: ")
# if name.lower() == "matej":
#     print("You have reached Mocka Man. Please send your complaints at mocka@man.com")
# else:
#     print("Wrong address. Please go away.")
#
# print("End")
#
# day = input("Enter the day of the week: ").lower()
# if day == "sunday":
#     print("YAY! REST AND RELAXATION!")
# elif day == "saturday":
#     if input("Are you on the job? Type Y for yes and anything else for no ") == "Y":
#         print("GO HOME!")
#     else:
#         print("PARTAYYYYYY!")
# elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
#     print("Boooooooring!")
# elif day == "friday":
#     print("ITS FRIDAY NOOOOOOW TM TM TM TMMT TMMTMTMTMT! 👩🏿‍🦲")
# else:
#     print("You are such an idiot. Go learn the days of the week and come back again. Bye.")
#
# print("The end of my code is here")
#
# word = input("Enter a word: ")
#
# if len(word) > 5:
#     print("Long word")
# elif word.lower() == "hi":  # if we add the word goodday instead of hi, it will actually trigger the first if only
#     print("Hey yorself")
# else:
#     print("Word was not hi and was shorter than 5 characters!")

# CTRL + / -> Comments everything
# CTRL + A -> Select all
# something() -> Function call
# something -> value

# Loops
# If you see that results are running indefinitely, you might have an infinite loop
# iterations = 10
# i = 0
#
# while i < iterations:
#     print(i)
#     i = i + 1 # If you comment this out, your code will loop infinitely
#
# print("End of while. We continue with our lives.")
#
# # While with an unpredictable case
#
# while input("What is your favorite color?") != "Red":
#     print("That is a horrible favorite color. Please choose another one!")
#
# print("That is better. Red is awesome!")
# #
# # 1. python sees a while and prepares to loop
# # 2. python tries to calculate the statement ( question )
# # 3. python sees input() function and in order to get a result it executes it
# # 4. input() is executed and waits for the user to enter something
# # 5. after user enters something ( Ex: "Yellow" ) the input returns the value ( "Yellow" ) as a result
# # 6. python can now compare the value with the hardcoded value "red" (Ex: "Yellow" != "Red")
# # 7. Since "Yellow" is not equal to "Red" the statement is True and the while loop block code is executed
# # 8. python executes the print() method in the while loop block
# # 9. python returns to the while to do the same again
# # 10. if at some point the input() returns "Red", python will skip the block and continue forward, executing the print outside of the while block
#
# # # Arrays
# # # Array is a collection of data values
# # # Array is written with [ ]
# # # Indexes start from 0
# # # 0 -> 2, 1 -> 3, 2 -> 5
# numbers = [2, 3, 5]
# strings = ["Bob", "Jill", "Wayne"]
# # Take a value from an array
# print(numbers[0])  # We would get the first item from the numbers array
# print(strings[1])
#
# print(len(strings))  # gives you how many items are in an array
#
# numbers[2] = 100  # We can change the value of some item by it's index
# print(numbers)
#
# # numbers[4] = 200  # We can't add values to indexes that do not exist
# # print(numbers)  # This will throw an error
#
# numbers.append(12)  # Adds new item at the end
# print(numbers)
#
# strings.pop()  # Removes one item from the end
# print(strings)
#
# numbers.insert(1, 1000)  # Adds an item to an index and pushes all items forward
# print(numbers)
#
# strings.clear()  # clears the array of all items
# print(strings)
#
# print(numbers.index(3))  # opposite of numbers[2], you give it value and it finds on which index it is
# print(numbers.index(111111))  # if it is not found it will return an error
#
# numbers.reverse()  # reverses the order of the items, but it changes the original array
# print(numbers)
#
# # How to reverse an array without touching the original ( this works for all functions that change the original )
# numbers2 = numbers.copy()  # we copy the original to another variable so we can change the other variable
# numbers.reverse()
# print(numbers)
# print(numbers2)
#
# print(1000 in numbers)  # this statement returns true or false, if it finds the value in the array
# print(340 in numbers)
#
# print(numbers.count(1000))  # this function counts how many times the value is found
# print(numbers.count(111111))  # this function counts how many times the value is found
#
# # Combining Arrays with loops
# dogs = ["Sparky", "Toto", "Molly", "Whiskers", "Rex"]
# i = 0
#
# while( i < len(dogs)):
#     if(dogs[i] == "Whiskers"):
#         print("WTF. This is a cat.")
#         i = i + 1
#         # break  # Stop the loop right now and continue with the other code
#         continue  # Stops the current iteration from continuing and skipping right back to the while statement
#     print("Dog was found:")
#     if(dogs[i] == "Molly"):
#         print(f"{dogs[i]} is a good gurl")
#     else:
#         print(f"{dogs[i]} is a good boi")
#     i = i + 1
#
# print("That is all the doggos!")
#
# dogs = ["Sparky", "Toto", "Molly", "Whiskers", "Rex"]
#
# for dog in dogs:  # for variable_name in collection_name ( every item one by one is stored in the variable )
#     print(dog)
#
# i = 0
# while i < len(dogs):
#     print(dogs[i])
#     i = i + 1

# # Example 1
# # We want to find all values that are not from 1 to 5
# answers = [1, 2, 5, 3, 5, 1, 2, 5, 10, 7, 1, 2, 2, 2, 2, 2, 2, 5, 3, 5, 1, 2, 5, 1, 2, 5, 3, 5, 1, 2, 5, 10, 7, 1, 2, 2, 2, 2, 2, 2, 5, 3, 5, 1, 2, 5, 1, 2, 5, 3, 5, 1, 2, 5, 10, 7, 1, 2, 2, 2, 2, 2, 2, 5, 3, 5, 1, 2, 5]
# i = 0
# brokenAnswers = []
# while(i < len(answers)):
#     if(answers[i] <1 or answers[i] > 5):
#         brokenAnswers.append(answers[i])
#     i = i + 1
#
# print(brokenAnswers)
# print(f"We found 10 this many times -> {answers.count(10)}")
# print(f"We found 5 this many times -> {answers.count(5)}")

# Functions

# Example without function
# numberOne = 5
# numberTwo = 10
#
# if numberOne > numberTwo:
#     print("First number is larger!")
# if numberTwo > numberOne:
#     print("Second number is larger!")
# else:
#     print("They are equal!")

# Problem no. 1
# Values are fixed
# If we want to work with some other numbers, we have to change the code it self
# Problem no. 2
# If we need this again, we need to rewrite the whole block of code so we can use it in another place
# Problem no. 3
# When we change something in the code, we have to change it everywhere else


# Functions
# A function is a reusable block of code that we can reuse and call anywhere anytime
# Function has an input and output
# It must first be defined so we can call it later
# Defined function is not executed without calling it first by name
# return always returns 1 thing
# We can have multiple or none parameters
# Parameters are the placeholders for values that the function needs from the outside ( whoever is calling it (
# Arguments are the values that are given to the parameters by the person calling the function
# Function can have no return. This function is called void function and does not have any resulting value
#
# The function below is a function without parameters
#
#
# def say_hello():  # This is how we define a function
#     print("Hi!")
#     print("How are you?")
#
#
# say_hello()  # This is how we call a function
#
#
# def compare_two_numbers(number1, number2):
#     print("Function starting...")
#     if number1 > number2:
#         print("First number is larger!")
#     if number2 > number1:
#         print("Second number is larger!")
#     else:
#         print("They are equal!")
#     print("Function ending...")
#
#
# what_is_returned_from_void = compare_two_numbers(5, 10)  # This is how we call a function with parameters and we give arguments to the parameters
# compare_two_numbers(2, 6)
# compare_two_numbers(100, 2)
# compare_two_numbers(1, 1)
# print("-----------------------")
# print(what_is_returned_from_void)
# print("-----------------------")

#
# def calculate_average(number1, number2, number3):
#     sum = number1 + number2 + number3
#     average = sum / 3
#     return average
#     print("this will not execute")  # After return, nothing is executed, the function exits at return keyword
#
#
# result = calculate_average(2, 4, 6)
# print(result)
#
#
# def calculate_sum_and_subtract(number1, number2):
#     sum = number1 + number2
#     sub = number1 - number2
#     return [sum, sub]
#
#
# col_result = calculate_sum_and_subtract(4, 7)  # When function is done: col_result = [11, -3]
# print(col_result)


# 1. Define a variable col_result
# 2. Call the function named calculate_sum_and_subtract with 4 and 7 arguments
# 3. Python finds the function by name on line 330
# 4. Python adds 4 to the parameter number1 and adds 7 to the parameter number2
# 5. Then python executes the lines of code in the function
# 6. When it hits return it grabs the value [sum, sub] and exits the fucntion
# 7. The value from return is replaced on the spot where we called the function calculate_sum_and_subtract
# 8. Python adds that resulting value in the col_result variable


# Edge case
#
#
# def find_seven(array_of_numbers):
#     for num in array_of_numbers:
#         print(num)
#         if(num == 7):
#             return True  # return will bypass the whole loop and the loop or any code under return will not continue
#
#     print("The number was not found")
#     return False
#
#
# print(find_seven([1, 2, 3, 4, 5]))
# print(find_seven([1, 2, 7, 4, 3]))

# Code should be read as a paper
# This is a sample of some code that looks nice and is well written/organized with functions
# def get_students_average_years(students):
#     student_years = filter_only_student_years(students)
#     student_average_years = student_years.sum() / len(student)
#     return student_average_years
#
#
# students = get_students_from_excel("c://documents/studies/first_study/students.xls")
# students_average_years = get_students_average_years(students)
# print(students_average_years)
#
#
# Object Oriented Programming
#
# Human problem: Order a pizza
#
# Human solution:
# Get list of pizzas
# Get details and prices
# Make an order
# Give information of address and billing
# Wait for the pizza
# Eat the pizza
#
# Defining objects for a machine to understand:
#
# Define Object Topping
# Topping has details like type, price, name
# Define Object Pizza
# Pizza has details like type, name, price, size, toppings
# Define Object Address
# Address has details like street, number, floor
# Define Object Billing
# Billing has details like type, number, name, exp
# Define Object Order
# Order has details like delivery date, Address, Name, price, pizzas, billing type
#
# class Human:
#     def __init__(self, name, last):
#         self.name = name
#         self.last = last
#
#     def speak(self):
#         print(f"Hello! My name is {self.name}!")
#
#     def yell(self):
#         print("AAAAAaaaaaaaaaaaaaaAAAAAAAAAaaaaaaaa!")
# PascalCase


class Pizza:  # Defining a class with the name Pizza
    def __init__(self, name, size, cena):  # Constructor
        # Here we create 3 properties to the object that is currently being constructed
        self.name = name  # property
        self.size = size
        self.price = cena

    def get_receipt(self):
        print(f"The pizza {self.name} with size {self.size} costs {self.price}$!")


capri_pizza = Pizza("Capri", "XL", 20)  # This is an object pizza created from a class Pizza with some properties
pepperoni_pizza = Pizza("Pepperoni", "S", 5)

print(capri_pizza.size)
capri_pizza.get_receipt()
pepperoni_pizza.get_receipt()

math_subject_students = []


class Subject:
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules


class Major:
    def __init__(self, name, subjects, classes):
        self.name = name
        self.subjects = subjects
        self.classes = classes


class Student:
    def __init__(self, first_name, last_name, age, gpa, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa
        self.year = year
        self.major = major

    def identify_student(self):
        print(f"Student {self.first_name} {self.last_name} is {self.age} years old and has {self.gpa} gpa!")

    def get_student_major_info(self):
        print(f"{self.first_name} is majoring in {self.major.name} and has {len(self.major.subjects)} subjects")
        print(f"The first subject for this student is {self.major.subjects[0].name}")

    def enroll_student_in_math(self):
        math_subject_students.append(self)


subject_psychology = Subject("Psychology 101", 10)
subject_emotions = Subject("Emotions", 8)

major_behavioural_psychology = Major("Behavioural Psychology", [subject_psychology, subject_emotions], 40)

matej = Student("Matej", "Trojacanec", 33, 0, 1, major_behavioural_psychology)

matej.identify_student()
matej.get_student_major_info()
print(f"Matej has this many modules in his second subject: {matej.major.subjects[1].modules}")
students = []
students.append(matej)

# Class Human
# Properties : full_name, age, address
# Method : say_hi -> which prints this text in the console: "The human {full_name} says hi!"
# Class Dog
# Properties: name, race, age, owner( Human )
# Method : bark -> which prints this text in the console: "BARK BARK BARK"

# Create two human objects of Dragan and Matej
# Create two dog objects of Toto and Moli
# Make sure that they have the right owner






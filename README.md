# Hello Python 🐍

## Navigation

* [Instalation](#installation)
* [Creating a PyCharm project](#creating-a-pycharm-project)
* [Running a Python app](#running-a-python-app)
* [PyCharm](#pycharm)
* [Practices](#practices)
* [Variables](#variables)
* [Data Types](#data-types)
* [Console](#console)
* [Arithmetic operators](#arithmetic-operators)
* [Comparison operators](#comparison-operators)
* [Logical operators](#logical-operators)
* [Code execution](#code-execution)
* [Working with strings](#working-with-strings)
* [If/Else](#ifelse)
* [Loops](#loops)
* [Collections/Arrays](#collectionsarrays)
* [Conversion](#conversion)
* [Functions and Methods](#functions-and-methods)
* [Importing modules](#importing-modules)
* [Modules](#modules)
* [Packages](#packages)
* [Resources](#resources)

## Installation

1. Go to the [python website](https://www.python.org/downloads/) and download the latest version of python
2. Install python by clicking next and checking the "Add Python to PATH" checkbox
3. Download PyCharm by going to the [jetbrains website](https://www.jetbrains.com/pycharm/) and picking the community edition
4. Install PyCharm and run the program to see if it works

## Creating a PyCharm project

1. Click on create a project
2. Make sure that the Base Interpreter is set to python 3.x ( Ex: 3.7 or 3.9 etc. )
3. You can now see a folder called "venv" and you might see a file named main.py
4. In case you don't see a file main.py, create a file yourself and name it main.py

## Running a Python app

1. Write some python code
2. Hit run on the PyCharm
3. Look at the results in the console

## PyCharm

* Green warnings -> Usually typos
* Yellow warnings -> Suggestions and good practices as well as conventions
* Red warnings -> Errors stating that the program will not work. You fucked up
* When you write . after a variable, it gives you all the methods you can use
* Lightbulb represents a suggestion on what to change in your code

## Practices

* underscore_case naming convention for functions, methods, variables, and parameters
* PascalCase naming convention for Classes
* Leave 2 empty lines after a function definition
* Leave 2 empty spaces after a comment in the same line of a code
* ; are not needed anywhere
* : means that we are starting a block of code

## Variables

* Temporary store data in the computer memory
* When storing numbers, they get converted in binary representation and then stored to a memory location
* Variables do not need declarator
* Variables can be rewritten at any time ( top-down execution will make sure the last change is remembered only )
* Variables should be written in lowercase
* Underscore convention?
* = - used for assigning value to a variable
* We can assign multiple variables at once by separating them with a ","

## Data Types

* string -> "" or ''
* integer -> standard numbers
* float -> separated with .
* boolean -> True or False
* types can't be mixed, they must be converted
* type() -> Tells you what type is a variable or value

```python
number = 25           # number
name = "Bob"          # string
last = 'Bobsky'       # string
isValid = True        # boolean
I_NvAlid = "Nope"     # bad naming not by convention. Don't do this ( this will work, but it's bad practice )
a, b, c = 2, 4, 3     # assign multiple values to multiple variables at the same time
z = x = v = 2         # assigning all variables at the same time
```

## Console

* Python code is executed in the console and you can see the results there
* The console works by having the text written in it ( strings )
* It can accept input, but that input is also always text ( strings )
* print("Some Text") -> function that prints stuff in the console
* input("Question for some input? ") -> function that requests for input in the console and returns the input as a result of type string

```python
print("Hello Human!")   # printing some text
print(32)               # printing some number
print(name)             # printing some variable value

something = input("Write something: ")  # whatever the person writes, is saved in the "something" variable
print(something)                        # using whatever the user gave us to do some stuff with it ( In our case, just print it )
```

### Example

```python
input_name = input("What is your name? ")
input_quest = input("What is your quest? ")
input_fav_color = input("What is your favorite color? ")

print("--------------------")
print("The knight name is:")
print(input_name)
print("His quest is:")
print(input_quest)
print("His favorite color is:")
print(input_fav_color)
print("--------------------")
print("He is so brave!")
```

## Arithmetic operators

* The + and - signs are doing the standard arithmetic functions
* The / sign is division and returns a float number
* The % sign is division that returns only the remainder of the division
* The * sign is multiplication
* The ** sign is power of something
* The // sign is division, but it rounds to the lower number
* += sign first sums up and then returns the result at the same time ( shorthand operator )
* We can use () brackets to apply precedent first
* Precedent:
  1. Brackets
  2. Exponentiation
  3. Multiplicaiton or Division
  4. Addition or Subtraction
* Functions for working with numbers
  * Mathematical functions can be imported with: import math
  * round(number) -> Rounds a number to the closest decimal
  * abs(number) -> Returns an absolute of a number ( always returns a positive number )
  * math.floor(number) -> Rounds to the lowest decimal every time

```python
sum_of_two = 2 + 5                # we can sum two numbers
sum_of_multiple = sum_of_two - 1  # we can get the result of the first sum and subtract something
print(sum_of_multiple)            # check the value in the console

cubed = 2**3                      # 2 to the power of 3
division_rounded = 9//2           # division but rounded to the lowest number
modulus = 9 % 2                   # division but it returns the left out part of the division

print(cubed)
print(division_rounded)
print(modulus)
```

## Comparison operators

* Operator > -> Larger
* Operator >= -> Larger or equal
* Operator < -> Lesser
* Operator <= -> Lesser or equal
* Operator == -> Equal
* Operator != -> Not Equal

## Logical operators

* and -> T + T = T, otherwise F
* or -> F + F = F, otherwise T
* not -> not F = T, not T = F

```python
five_is_larger = 5 > 1      # finds out if the statement is true or false and adds the boolean value in the variable
numbers_are_equal = 3 == 3  # since we are using = for assignment, for equals we use ==
ten_is_smaller = 10 <= 23   # finds if the number is lower or equal and adds the boolean value in the variable

five_is_larger_than_two_numbers = 5 > 2 and 5 > 1  # if both of them are true, then it is true
one_is_either_larger_or_smaller = 1 > 5 or 1 < 55  # if none of them is true then it is false

five_not_larger = not five_is_larger               # negation only flips the value of a variable ( T -> F or F -> T )

print(five_is_larger)
print(numbers_are_equal)
print(ten_is_smaller)
print(five_is_larger_than_two_numbers)
print(one_is_either_larger_or_smaller)
print(five_not_larger)
```

## Code execution

* When we click run it runs an interpreter
* Line by line from the top executes
* Defining a string is defining a series of characters
* Expressions are pieces of code that produce some value
* Python will first evaluate an expression that is last and then go backward
* Integer number and string number are not the same

```python
question = "Enter your name: "        
# python stores the string into a memory location

input_name = input(question.upper())  
# python then tries to fill in this variable but sees that there is no value, but a function called input()
# python executes input() and sees that it has a parameter
# python tries to send the attribute to the function but sees that the value is connected to a method that needs to be called
# python calls the method upper() and that method returns an uppercase value for the attribute question
# python gives the value of question uppercased to the function input and the function input is executed
# the method input waits until someone enters some text in the console
# when the text is entered the input() function finishes and a result is returned in the form of a string ( the text the person entered )
# python stores that result string to the input_name variable

print("Hello there " + input_name)
# python tries to call the function print()
# python sees that there is a parameter and tries to get the attribute for the function
# python sees that the attribute is an expression
# python executes the expression and connects both of the strings together
# python then sends the result of the expression as an attribute to the function print()
# print() shows the text in the console
```

## Working with strings

* Concatenation is done with +
* Escaping characters is done with \
* Single and double quotes can be used if we need to use the ones or others into the string itself
* Multiple lines string is done with 3 x " or 3 x ' ( Ex: """ This string can be in multiple lines! """ )
* A python string is indexed by character and starts from 0
  * You can get a python character from a string by using string[index]
  * Negative number indexes go from the back ( Ex: -1 index is the last character )
  * You can get multiple characters from a string by using string[index:characters] ( Ex: string[0:5] - Returns first 5 characters )
  * If you leave the index empty, the python interpreter will execute the expression as if there was a 0 there
  * If both are empty, it will just get all the characters ( string[:] )
* Strings can be formatted with adding f before the string and use variables within {} brackets ( Ex: f"Hello {name}!" )
* len(string) -> function that returns how many characters is in a string ( function can be used for any other collection )
* string.upper() -> Converts a string in to an upper case
* string.lower() -> Converts a string in to a lower case
* string.title() -> Converts a string in to Upper Case First Letters
* string.find(string) -> Will return the index of the first occurrence of that character ( Is case sensitive ) and will return -1 if it does not find anything
* string.replace(replacedString, newString) -> Finds occurrence in a string and replace all with a new string
* in operator -> finds if something is contained in something else, it returns true or false ( Ex: "Cool" in some_string )
* string.split(separator) -> Separates a string into a collection of strings depending on the separator

```python
name = "Bob"
last = "Bobsky"
full_name = name + " " + last  # We can connect two strings with +
another_full_name = f"{name} {last} is built differently than the previously named: {full_name}"  # another way of concatenation
broken_full_name = name + last  # If we don't leave empty space it will connect the words
legit_statement = " is awesome"
another_legit_statement = 'Bob is "smart"'  # We use '' quotes to have "" quotes in a string and vice versa
weird_stuff = "this is a qutation mark - \" and also this - ' "
# If we want treat a character as text we use \ before it ( \ is called escape character )

print(full_name)
print(broken_full_name)
print(full_name + legit_statement)
print(another_legit_statement)
print(another_full_name)

# We can treat strings as array of characters
print(len(full_name))        # len(my_string) is a function that returns how many characters are in a string
print(full_name[0])          # we can get any character from a string by its index ( in our case index 0 or the first letter )
print(full_name.lower())     # we can make a string in lowercase with this method
print(full_name.upper())     # we can make a string in uppercase with this method
print(full_name.split("a"))  # we can split a string by a character and get an array of strings
```

## If/Else

* If statement: -> if statement is True then execute all the lines below that are written in indentation
* Elif statement: -> Goes after an if statement and if the first if statement is false, this one follows and has the same rules as the if
* else: -> Goes at the end of an if the chain and executes if all if statements above fail

```python
name = input("Enter your name: ")
if name.lower() == "bob":
    print("You have reached Bob Bobsky. Please send your complaints at bob@bobsky.com")
else:
    print("Wrong address. Please go away.")

print("End")

day = input("Enter the day of the week: ").lower()
if day == "sunday":
    print("YAY! REST AND RELAXATION!")
elif day == "saturday":
    if input("Are you on the job? Type Y for yes and anything else for no ") == "Y":
        print("GO HOME!")
    else:
        print("PARTAYYYYYY!")
elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
    print("Boooooooring!")
elif day == "friday":
    print("ITS FRIDAY NOOOOOOW TM TM TM TMMT TMMTMTMTMT! 👩🏿‍🦲")
else:
    print("Go learn the days of the week and come back again. Bye.")

print("The end of my code is here")

word = input("Enter a word: ")

if len(word) > 5:
    print("Long word")
elif word.lower() == "hi":  # if we add the word goodday instead of hi, it will actually trigger the first if only
    print("Hey yorself")
else:
    print("Word was not hi and was shorter than 5 characters!")
```

## Loops

* Executing block of code multiple times
* while conditioning: -> Loops as long as the condition is true
* for an item in collection/string: -> Loops a collection and every item is placed in the item variable ( can be called anything )
* You can nest loops but remember that the counter names need to be different
* If you see that results are running indefinitely, you might have an infinite loop
* You can stop a loop or skip an iteration with these commands:
  * break
    * After this keyword the loop stops
    * All code after the keyword is skipped
    * All iterations after this iteration are also skipped
  * continue
    * After this keyword, the current iteration is skipped
    * All code after the keyword is skipped
    * All iterations after this iteration continue, and are not skipped
  * Remember that if you have a counter after the continue or break, it will not execute and you might get an infinite loop

```python
# While with predictable case
iterations = 10
i = 0

while i < iterations:
    print(i)
    i = i + 1 # If you comment this out, your code will loop infinitely

print("End of while. We continue with our lives.")

# While with an unpredictable case

while input("What is your favorite color?") != "Red":
    print("That is a horrible favorite color. Please choose another one!")

print("That is better. Red is awesome!")

# 1. python sees a while and prepares to loop
# 2. python tries to calculate the statement ( question )
# 3. python sees input() function and in order to get a result it executes it
# 4. input() is executed and waits for the user to enter something
# 5. after the user enters something ( Ex: "Yellow" ) the input returns the value ( "Yellow" ) as a result
# 6. python can now compare the value with the hardcoded value "red" (Ex: "Yellow" != "Red")
# 7. Since "Yellow" is not equal to "Red" the statement is True and the while loop block code is executed
# 8. python executes the print() method in the while loop block
# 9. python returns to the while to do the same again
# 10. if at some point the input() returns "Red", python will skip the block and continue forward, executing the print outside of the while block

```

## Collections/Arrays

* Array is a collection of data values
* Array is written with [ ]
* Indexes start from 0
* [1, 2, 3] -> Array or Collection of numbers
* range(10) -> Returns a range of numbers ( from 0 to 10 in our example )
* range(5, 10) -> Returns range from one to another number ( From 5 to 9 in our example )
* range(5, 10, 2) -> Returns a range from one to another number but steps a certain ammount of numbers every time ( 5, 7 and 9 in our example )
* collection[index] -> Get index
* collection[index:rangeIndex] -> Gets all items from the index to the rangeIndex ( Without the last )
* collection[:rangeIndex] -> If the index is left out, it defaults to 0
* collection[:] -> 0 to the end
* collection[index] = newValue -> Changing a value in a collection
* Methods
  * collection.append(item) -> adds a new item at the end of the collection
  * collection.insert(index, item) -> adds a new item at the index provided ( index 0 adds a new item at the front of the collection )
  * collection.clear() -> Empties a list
  * collection.pop() -> Removes the last item of the list
  * collection.index(item) -> Returns the index of the first occurance of the item provided ( Throws error if the item does not exist )
  * item in collection -> returns true or false if the item exist in the collection or not
  * collection.count(item) -> Returns the occurances of the item in the collection
  * collection.sort() -> Sorts the collection in place ( the collection is changed and sorted, but the method does not return anything )
  * collection.reverse() -> Reverses the collection
  * collection.copy() -> Creates a copy of the collection and returns it
* for "item" in "collection": -> A loop that does not have a counter and is designed to loop through collections one by one

```python

numbers = [2, 3, 5]
strings = ["Bob", "Jill", "Wayne"]

# Take a value from an array
print(numbers[0])  # We would get the first item from the numbers array
print(strings[1])

print(len(strings))  # gives you how many items are in an array

numbers[2] = 100  # We can change the value of some item by its index
print(numbers)

# numbers[4] = 200  # We can't add values to indexes that do not exist
# print(numbers)  # This will throw an error

numbers.append(12)  # Adds new item at the end
print(numbers)

strings.pop()  # Removes one item from the end
print(strings)

numbers.insert(1, 1000)  # Adds an item to an index and pushes all items forward
print(numbers)

strings.clear()  # clears the array of all items
print(strings)

print(numbers.index(3))  # opposite of numbers[2], you give it value and it finds on which index it is
print(numbers.index(111111))  # if it is not found it will return an error

numbers.reverse()  # reverses the order of the items, but it changes the original array
print(numbers)

# How to reverse an array without touching the original ( this works for all functions that change the original )
numbers2 = numbers.copy()  # we copy the original to another variable so we can change the other variable
numbers.reverse()
print(numbers)
print(numbers2)

print(1000 in numbers)  # this statement returns true or false if it finds the value in the array
print(340 in numbers)

print(numbers.count(1000))  # this function counts how many times the value is found
print(numbers.count(111111))  # this function counts how many times the value is found

# Combining Arrays with loops
dogs = ["Sparky", "Toto", "Molly", "Whiskers", "Rex"]
i = 0

# While loop with if case logic
while( i < len(dogs)):
    if(dogs[i] == "Whiskers"):
        print("WTF. This is a cat.")
        i = i + 1
        # break  # Stop the loop right now and continue with the other code
        continue  # Stops the current iteration from continuing and skipping right back to the while statement
    print("Dog was found:")
    if(dogs[i] == "Molly"):
        print(f"{dogs[i]} is a good gurl")
    else:
        print(f"{dogs[i]} is a good boi")
    i = i + 1

print("That is all the doggos!")

dogs = ["Sparky", "Toto", "Molly", "Whiskers", "Rex"]

# For in loop
for dog in dogs:  # for variable_name in collection_name ( every item one by one is stored in the variable )
    print(dog)

# While loop that does the exact same thing as the For in loop
i = 0
while i < len(dogs):
    print(dogs[i])
    i = i + 1
```

## Conversion

* In programming languages values of different types can't work together often
* Anything that we concatenate with a string, becomes a type string
* Output of a console also always returns a string, even if you enter a number
  * numbers as input in the console will result in a number from type string Ex: "3" or "22"
* Converting helps to transform value from one to another type if the value is valid in both types
  * Ex: We can convert "3" -> 3, but we can't convert "three" -> 3
* Failing to convert a value will throw an error
* Converting methods:
  * int() -> Convert string in to integer
  * float() -> String or number to a float
  * boolean() -> String in to boolean

```python

birth_year = input("Birth Year: ")
print(type(birth_year))  # Check to see that the type is string
converted_birth_year = int(birth_year)  # We convert the string to int
age = 2019 - converted_birth_year  # We calculate estimated age
print(type(age))  # We print the type of the age variable
print(age)  # We print the estimated age
```

## Functions and Methods

* Often there is code that we need to use multiple times on multiple places
* To not repeat the same piece of code everywhere which has some downsides, we want to reuse a piece of code
  * Not using functions, makes the code larger and less readable
  * The same code in 10 places instead of a function would be hard to maintain if you need to change it ( changes are in 10 places )
  * With a function, you can change 1 thing in 1 place ( in the function ) and all the places that use the function will also be using the change
* A reusable piece of code that we can define and then call whenever we need it is called a function
  * Function definition -> We write the code that we want to use later, name the function, define what it needs and what it gives back
    * When we define a function IT IS NOT EXECUTED. Just added in memory.
    * A definition is done with the keyword "def", the name of the function next and then () with parameters in them or nothing if there are no parameters
  * Function executing ( calling ) -> We execute the function when we call the name of the function and provide whatever it needs
    * Execution is done at the line of code where the function is defined. If we call it 100 times, 100 times will go to that same line
* Functions have a simple flow: They get input and return output
  * Getting input is done through parameters and arguments
    * Parameters are the variables in the function definition that expect some value
    * Arguments are the values that are passed to the function at the parameters places when the function is called
  * Returning output is done with the "return" keyword and after the keyword a value we want to return
    * There can only be 1 value returned from a function
    * There can be multiple returns in a function
    * When a return is hit, the function returns a value and exits the function completely, not executing code after that line
    * The place where we called the function, would be replaced with the value we returned
* Function is a general-purpose python function
* Method is a function that is attached to some object

```python
def greet_user(first, last):
    print(f"Hi {first} {last}!")

greet_user("Bob", "Bobsky")
greet_user("Jill", "Wayne")
```

## Importing modules

* Modules are like libraries or packages
* It is a packet of reusable functions
* Modules are used for better organization and reusability
  * Ex: If you have functions for reading from an excel file you might create a module for that, so every time you need to read from an excel you can just import the module
* There are the python native modules and external modules that you download and import, but you can also create your own modules
* import module_name -> Imports a module ( Ex: import math -> Imports the math module )

```python
import math  # importing the module here by name

print(math.pi)  # using a value from the module
print(math.sqrt(9))  # using a method from the module
```

## Modules

* Module is a file that contains some python code
* We use these modules to make different files for organizational purposes and structure
* We can also reuse one file in multiple places, making our code reusable and preventing duplicate code
* How to create a module:
  * Create a file
  * Add some methods or classes to it
* How to import a module:
  * Go to another file
  * Write import and the name of the file ( Without the .py extension )
  * Importing the whole file will give you an object with the name of the file from where you use the methods and classes
  * You can also use the methods or classes by name, but you have to explicitly name the method or class you want to use in the import

```python
# Module called calculating_utilities.py
def sum(x, y):
    return x + y


def suptract(x, y):
    return x - y


def concat(x, y):
    return str(x) + str(y)

```

```python
# Standard import of the whole file in this object
import calculating_utilities

print(calculating_utilities.sum(2, 3))
print(calculating_utilities.suptract(2, 3))
print(calculating_utilities.concat(2, 3))

# Import of a certain method that we can use now without the object
import calculating_utilities
from calculating_utilities import sum

print(sum(2, 3))
```

## Packages

* A package is a folder, a module is a file
* A package is a section of the code
* A package contains modules
* When we put a module in a package, we can't just call the module on its own. We have to import the package first
* How to create a package:
  * Create a new directory and name it related to some domain of the program that you are writing
  * In the directory create a file called \__init__.py ( a file that marks the folder and everything in it as a package )
    > Hint: PyCharm already has an option of creating the file and the directory together called: New -> Python Package
  * Add new modules in the package and write some functions or classes in the modules
* How to import a package:
  * Go to a file where you need the package
  * Write import and then the name of the package followed by a "." and then the module name (Ex: import print_utils.messaging )
  * You can independently import functions to use without the prefix with from ( Ex: from print_utils.messaging import error, success)
  * You can also just import 1 module or multiple and use the modules without the package prefix ( Ex: from print_utils import messaging)

```python
# Module called messaging.py in a folder called string_utils
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def error(message):
    print(bcolors.FAIL + message)


def success(message):
    print(bcolors.OKGREEN + message)
```

```python
# Importing from a package and inside it a module
import string_utils.messaging

string_utils.messaging.error("Problem!")
string_utils.messaging.success("Yay!")

# Importing from a package and module, but only certain methods
import string_utils.messaging
from string_utils.messaging import error, success

error("Problem!")
success("Yay!")

# Importing from a package and targeting directly a module
import string_utils.messaging
from string_utils import messaging

messaging.error("Problem!")
messaging.success("Yay!")
```

## Resources

* [Official Documentation](https://docs.python.org/3/)
* [Module Index](https://docs.python.org/3/py-modindex.html)
* [Python tutorial](https://www.youtube.com/watch?v=_uQrJ0TkZlc)
* [Python problems website](https://www.hackerrank.com/domains/python)

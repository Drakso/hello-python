# Python

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
* When you write . after a variable it gives you all the methods you can use
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
* The console works by having text written in it ( strings )
* It can accept input, but that input is also always text ( strings )
* print("Some Text") -> function that prints stuff in the console
* input("Question for some input? ") -> function that requests for an input in the console and returns the input as a result of type string

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
* The ** sign is power of sign
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
# python stores the string in to a memroy location

input_name = input(question.upper())  
# python then tries to fill in this variable, but sees that there is no value, but a function called input()
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

## Resources

* [Official Documentation](https://docs.python.org/3/)
* [Module Index](https://docs.python.org/3/py-modindex.html)

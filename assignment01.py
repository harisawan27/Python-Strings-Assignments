# -*- coding: utf-8 -*-
"""Assignment01.ipynb

**Muhammad Haris Awan**

**00279605**

**Class Assignment 1**

# Python Strings Assignments

Part 1: Understanding String Literals
1. Create three different strings using each type of quotation:
* Single quotes ('example')
* Double quotes ("example")
* Triple quotes ('''example''')
"""

# Single qoutes
single_qoutes = 'Hello World'
print(single_qoutes)

# Double qoutes
double_qoutes = "Hello World"
print(double_qoutes)

#Single qoutes
triple_qoutes = """I am Haris
I study in class 11
I learning Python in GIAIC"""
print(triple_qoutes)

"""2. Explain in your own words: What is the advantage of each type of quotation?

Advantages of each type of quotation:
 - Single quotes are simple and useful for short strings.
 - Double quotes allow embedding single quotes inside.
 - Triple quotes are useful for multi-line strings and documentation.

3. Write a string that contains both single and double quotes inside it.

Example: She said,
"I'm going to the store."
"""

mixed_strings = """ He said, "I'm going to play Cricket." """
print(mixed_strings)

"""4. Create a multi-line string using triple quotes that describes your favorite hobby.

"""

my_hobby = """
I love programming because it allows me to create amazing applications.
It challenges my logic and problem-solving skills while making a positive impact.
"""
print(my_hobby)

"""# Part 2: String Methods Practice

1. Create a variable full_name with your full name (first and last name). Then write code
to:
* Print your name in all uppercase letters
* Print your name in all lowercase letters
* Print your name with the first letter of each name capitalized
"""

full_name = "Muhammad Haris Awan"
print(full_name.upper())       # Uppercase
print(full_name.lower())       # Lowercase
print(full_name.title())       # Capitalized

"""2. Create a variable messy_text = " Python programming is fun! " Then write code
to:
* Remove all the extra spaces at the beginning and end
* Replace "fun" with "amazing"
* Count how many times the letter 'i' appears
"""

messy_text = " Python programming is fun! "

striped = messy_text.strip()      # Remove extra spaces
print(striped)

replaced = striped.replace("fun", "amazing")  # Replace words
print(replaced)

counted = messy_text.count("i")   # Count occurrences of 'i'
print(counted)

"""3. Create a variable sentence = "The quick brown fox jumps over the lazy dog"
Then write code to:
* Split this sentence into a list of words
* Join the words back together with dashes between them
* Check if the sentence starts with "The"
* Find the position of the word "fox
"""

sentence = "The quick brown fox jumps over the lazy dog"

words = sentence.split()       # Split into words
print(words)

print("-".join(words))        # Join words with dashes

print(sentence.startswith("The"))  # Check if it starts with "The"

print(sentence.find("fox"))    # Find position of "fox"

"""# Part 3: F-Strings

1. Create variables for:
* Your name
* Your age
* Your favorite programming language

Then use f-strings to create these sentences:
* "My name is {your_name} and I am {your_age} years old."
* "I enjoy programming in {language}, it's my favorite!"
* Create a math expression inside an f-string: "In 5 years, I will be {age + 5} years
old."
"""

# Part 3: F-Strings
name = "Haris"
age = 17
language = "Python"

print(f"My name is {name} and I am {age} years old.")
print(f"I enjoy programming in {language}, it's my favorite!")
print(f"In 5 years, I will be {age + 5} years old.")

"""# Part 4: Combining String Methods with F-Strings

Create a program that:
1. Asks for user input about their first name, last name, and birth year
2. Uses string methods to properly capitalize their name
3. Uses f-strings to create a profile message: "Profile: {First Last}, Age: {calculated age},
Username: {first initial + last name + birth year}"
"""

first_name = input("Enter your first name: ").strip().capitalize()
last_name = input("Enter your last name: ").strip().capitalize()
birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year

username = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"
profile_message = f"Profile: {first_name} {last_name}, Age: {age}, Username: {username}"
print(profile_message)

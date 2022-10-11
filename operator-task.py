## Make example of python operator
x = 35
y = 5

# addition
print(x + y)

# subtraction
print(x - y)

# multiplication
print(x * y)

# division
print(x / y)

# modulus
print(x % y) ## outputs the remainder, 35/5 = 7, remainder 0

# exponentiation
print(x ** y) ## 35**5 = 35^5 = 52521875

# not equal
print(x != y) ## outputs True

# String Slicing
word = "Python"
print(word[0]) ## outputs P
print(word[5]) ## outputs n
print(word[-1]) ## outputs n
print(word[0:2]) ## outputs Py
print(word[2:5]) ## outputs tho
print(word[:2]) ## outputs Py

# Use the len() function to get the length of a string
# Use the strip() function to remove whitespace from the beginning or the end of a string

sentence = "   this is a sentence.   "
print(sentence.strip()) ## outputs "This is a sentence."

Example_text = "This is a sentence, with some words that make up the sentence."

# Find all instances of the word "sentence" in the string
print(Example_text.count("sentence")) ## outputs 2

# Change the case of the string to upper case
print(Example_text.upper())

# Change the case of the string to lower case
print(Example_text.lower()) 

# Capitalize the first letter of the string
print(sentence.capitalize())

# Replace all instances of one word in a string with another
print(sentence.replace("sentence", "Example_text")) ## outputs "This is a Example_text, with some words that make up the Example_text."

# Week 2

## Python Tasks

![Python Tasks](images/pythonTasks.png)

## Git & Github

### Git

Git is a version control system. It allows you to keep track of changes to your code. It also allows you to work on code with other people.

#### Git Commands

- `git init` - initialize a git repository
- `git status` - check the status of your repository
- `git add` - add files to the staging area
- `git commit -m "message"` - commit changes to the repository, with a message
- `git log` - view the commit history
- `git push` - push changes to a remote repository
- `git pull` - pull changes from a remote repository
- `git clone` - clone a remote repository

Tip: You can use `git help <command>` to get more information about a command.

### Github

Github is a website that hosts git repositories. It allows you to share your code with other people, and collaborate on projects.
Github also has a lot of useful features, like issue tracking, pull requests, and code reviews.

#### Github Commands

- `git remote add origin <url>` - add a remote repository
- `git push -u origin master` - push changes to the remote repository
- `git pull origin master` - pull changes from the remote repository

## Task 1 - Python Basics

### Task 1.1 - Variables

Variables are used to store data. In Python, variables are declared by assigning a value to a name. The name can be any valid identifier, and the value can be any valid Python expression. The assignment operator is `=`.

1. Create a variable called `name` and assign it the value of your name.
2. Create a variable called `age` and assign it the value of your age.

 ```python
name = "John"
age = 21
```

### Task 1.2 - Data Types

Python has five standard data types:

- String - a sequence of characters
- Integer - a whole number
- Float - a number with a decimal point
- Boolean - a value of either `True` or `False`
- List - a collection of values

1. Create a variable called `height` and assign it the value of your height.
2. Create a variable called `is_student` and assign it the value of `True`.
3. Create a variable called `subjects` and assign it the value of a list of your subjects.

 ```python
height = 1.8
is_student = True
subjects = ["Maths", "English", "Science"]
```

How to check the data type of a variable:

```python
print(type(height)) # expected output: <class 'float'>
print(type(is_student)) # expected output: <class 'bool'>
print(type(subjects)) # expected output: <class 'list'>
```

### Task 1.3 - Input

The `input()` function allows the user to enter data. The data entered is always a string.

```python
your_first_name = input("Please enter your first name: ")
your_last_name = input("Please enter your last name: ")
your_DOB = input("Please enter your date of birth: ")
your_course = input("Please enter your course: ")
your_uk_resident = input("Are you a UK resident? (True/False): ")

print(your_first_name, your_last_name, your_DOB, your_course, your_uk_resident)
# expected output: Abishek Aneese 26/07/2001 DevOps True
```

### Task 1.4 - Operators

Operators are used to perform operations on variables and values.

#### Arithmetic Operators

| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus | x % y |
| ** | Exponentiation | x ** y |
| // | Floor division | x // y |

#### Assignment Operators

| Operator | Name | Example | Same As |
| --- | --- | --- | --- |
| = | Assignment | x = 5 | x = 5 |
| += | Addition assignment | x += 3 | x = x + 3 |
| -= | Subtraction assignment | x -= 3 | x = x - 3 |
| *= | Multiplication assignment | x *= 3 | x = x * 3 |
| /= | Division assignment | x /= 3 | x = x / 3 |
| %= | Modulus assignment | x %= 3 | x = x % 3 |
| //= | Floor division assignment | x //= 3 | x = x // 3 |
| **= | Exponentiation assignment | x **= 3 | x = x ** 3 |
| &= | AND assignment | x &= 3 | x = x & 3 |
| ^= | XOR assignment | x ^= 3 | x = x ^ 3 |
| >>= | Right shift assignment | x >>= 3 | x = x >> 3 |
| <<= | Left shift assignment | x <<= 3 | x = x << 3 |

*Note:*

- There is also the or operator `|` which is used to perform a OR operation. eg: `x | y` will return `True` if either `x` or `y` is `True`.

- The right shift operator `>>` is used to shift the bits of a number to the right. 
- eg: `x >> 1` will shift the bits of `x` to the right by 1. When `x` is `5 (00000101)`, the result will be `2 (00000010)`.

#### Comparison Operators

| Operator | Name | Example |
| --- | --- | --- |
| == | Equal | x == y |
| != | Not equal | x != y |
| > | Greater than | x > y |
| < | Less than | x < y |
| >= | Greater than or equal to | x >= y |
| <= | Less than or equal to | x <= y |

#### Logical Operators

| Operator | Description | Example |
| --- | --- | --- |
| and | Returns True if both statements are true | x < 5 and  x < 10 |
| or | Returns True if one of the statements is true | x < 5 or x < 4 |
| not | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

#### Identity and Membership Operators

| Operator | Description | Example |
| --- | --- | --- |
| is | Returns True if both variables are the same object | x is y |
| is not | Returns True if both variables are not the same object | x is not y |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

#### Examples

```python
# Arithmetic Operators
x = 35
y = 5

print(x + y) # expected output: 40
print(x - y) # expected output: 30
print(x * y) # expected output: 175
print(x / y) # expected output: 7.0
print(x % y) # expected output: 0

x = 5
y = 2

print(x ** y) # expected output: 25
print(x // y) # expected output: 2

========================================
# Assignment Operators

x = 5
x += 3
print(x) # expected output: 8

x = 5
x *= 3
print(x) # expected output: 15

x = 5
x >>= 1
print(x) # expected output: 2

========================================
# Comparison Operators

x = 5
y = 3

print(x == y) # expected output: False
print(x != y) # expected output: True
print(x > y) # expected output: True
print(x < y) # expected output: False
print(x >= y) # expected output: True
print(x <= y) # expected output: False

========================================
# Logical Operators

x = 5

print(x > 3 and x < 10) # expected output: True
print(x > 3 or x < 4) # expected output: True
print(not(x > 3 and x < 10)) # expected output: False

========================================
# Identity and Membership Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # expected output: True
print(x is y) # expected output: False
print(x == y) # expected output: True

print("banana" in x) # expected output: True
print("pineapple" not in x) # expected output: True
```

## String Methods

### String Slicing

String slicing is used to get a part of a string. The syntax is:

```python
string[start:end:step]
```

- `start` is the index of the first character you want to get.
- `end` is the index of the first character you don't want to get.
- `step` is the number of characters you want to skip.

```python
string = "Hello World"
print(string[0:5]) # expected output: Hello
print(string[6:11]) # expected output: World
print(string[0:11:2]) # expected output: HloWrd
```

### String Casings

String casings are used to change the casing of a string. The syntax is:

```python
string.casing()
```

- `casing` is the casing you want to change to. It can be either `lower()`, `upper()`, `title()`, `capitalize()` or `swapcase()`.

```python
string = "Hello World"
print(string.lower()) # expected output: hello world
print(string.upper()) # expected output: HELLO WORLD
print(string.title()) # expected output: Hello World
print(string.capitalize()) # expected output: Hello world
print(string.swapcase()) # expected output: hELLO wORLD
```

### Modifying Strings with Methods

String methods are used to perform operations on strings. The syntax is:

```python
string.method()
```

- `method` is the method you want to use. It can be either `count()`, `find()`, `index()`, `replace()`, `split()`, `strip()`.

```python
string = "Hello World"
print(string.count("l")) # expected output: 3
print(string.find("l")) # expected output: 3
print(string.index("l")) # expected output: 2
print(string.replace("l", "L")) # expected output: HeLLo WorLd
print(string.split(" ")) # expected output: ['Hello', 'World']
print(string.strip("l")) # expected output: Hello Wor
```

### Concatenating Strings

String concatenation is used to join two or more strings. The syntax is:

```python
string1 + string2
```

```python
string1 = "Hello"
string2 = "World"
print(string1 + " " + string2) # expected output: Hello World
```

### Casting and F-Strings

Casting is used to convert a variable from one type to another. The syntax is:

```python
type(variable)
```

- `type` is the type you want to convert to. It can be either `int()`, `float()`, `str()`.
- `variable` is the variable you want to convert.

```python
x = 4
y = 4.0
z = "4"

print(int(y)) # expected output: 4
print(float(x)) # expected output: 4.0
print(str(x)) # expected output: 4
```

F-Strings are used to format strings. The syntax is:

```python
f"{variable}"
```

```python
name = "Abishek"
age = 21
print(f"My name is {name}, and I am {age}") # expected output: My name is Abishek, and I am 21
```

## Data Collections

### Lists

Lists are used to store multiple items in a single variable. The syntax is:

```python
list = ["item1", "item2", "item3"]
```

```python
list = ["DevOps", "Cloud", "Data Science"]
print(list) # expected output: ['DevOps', 'Cloud', 'Data Science']
```

#### List Methods

| Method | Description |
| --- | --- |
| append() | Adds an element at the end of the list |
| count() | Returns the number of elements with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the item with the specified value |
| sort() | Sorts the list |

```python
list = ["DevOps", "Cloud", "Data Science"]
list.append("Machine Learning")
print(list) # expected output: ['DevOps', 'Cloud', 'Data Science', 'Machine Learning']

list = ["DevOps", "Cloud", "Data Science"]
print(list.count("DevOps")) # expected output: 1

list = ["DevOps", "Cloud", "Data Science"]
list.insert(1, "Machine Learning")
print(list) # expected output: ['DevOps', 'Machine Learning', 'Cloud', 'Data Science']

list = ["DevOps", "Cloud", "Data Science"]
list.pop(1)
print(list) # expected output: ['DevOps', 'Data Science']

list = ["DevOps", "Cloud", "Data Science"]
list.remove("Cloud")
print(list) # expected output: ['DevOps', 'Data Science']

list = ["DevOps", "Cloud", "Data Science"]
list.sort()
print(list) # expected output: ['Cloud', 'Data Science', 'DevOps']
```

### Tuples

Tuples are used to store multiple items in a single variable, but they are immutable. The syntax is:

```python
tuple = ("item1", "item2", "item3")
```

```python
tuple = ("DevOps", "Cloud", "Data Science")
print(tuple) # expected output: ('DevOps', 'Cloud', 'Data Science')
```

#### Tuple Methods

| Method | Description |
| --- | --- |
| count() | Returns the number of times a specified value occurs in a tuple |
| index() | Searches the tuple for a specified value and returns the position of where it was found |

```python
tuple = ("DevOps", "Cloud", "Data Science")
print(tuple.count("DevOps")) # expected output: 1

tuple = ("DevOps", "Cloud", "Data Science")
print(tuple.index("DevOps")) # expected output: 0
```

### Dictionaries

Dictionaries are used to store data values in key:value pairs. The syntax is:

```python
dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

```python
dictionary = {
    "name": "Abishek",
    "age": 21,
    "country": "India"
}
print(dictionary) # expected output: {'name': 'Abishek', 'age': 21, 'country': 'India'}
```

#### Dictionary Methods

| Method | Description |
| --- | --- |
| fromkeys() | Returns a dictionary with the specified keys and values |
| get() | Returns the value of the specified key |
| items() | Returns a list containing a tuple for each key value pair |
| keys() | Returns a list containing the dictionary's keys |
| pop() | Removes the element with the specified key |
| popitem() | Removes the last inserted key-value pair |
| update() | Updates the dictionary with the specified key-value pairs |
| values() | Returns a list of all the values in the dictionary |

```python
dictionary = {
    "name": "Abishek",
    "age": 21,
    "country": "England"
}
print(dictionary.fromkeys("name", "Abishek")) # expected output: {'n': 'Abishek', 'a': 'Abishek', 'm': 'Abishek', 'e': 'Abishek'}
print(dictionary.get("name")) # expected output: Abishek
print(dictionary.items()) # expected output: dict_items([('name', 'Abishek'), ('age', 21), ('country', 'England')])
print(dictionary.keys()) # expected output: dict_keys(['name', 'age', 'country'])
print(dictionary.values()) # expected output: dict_values(['Abishek', 21, 'England'])

dictionary = {
    "name": "Abishek",
    "age": 21,
    "country": "England"
}
dictionary.pop("age")
print(dictionary) # expected output: {'name': 'Abishek', 'country': 'England'}

dictionary = {
    "name": "Abishek",
    "age": 21,
    "country": "England"
}
dictionary.popitem()
print(dictionary) # expected output: {'name': 'Abishek', 'age': 21}


dictionary = {
    "name": "Abishek",
    "age": 21,
    "country": "England"
}
dictionary.update({"name": "Aneese"})
print(dictionary) # expected output: {'name': 'Aneese', 'age': 21, 'country': 'England'}
```

#### Task

```python

story1 = { "start": "Once upon a time", "middle": "Angel baked Luke bread ", "end": "the end" }
print("=====================================\n")

print(story1)
print(type(story1))

print("=====================================\n")

print(story1.keys())
print(story1.values())

print("=====================================\n")

print(story1["start"])
print(story1["middle"])
print(story1["end"])

print("=====================================\n")
story1["hero"] = "Shahrukh"
print(story1)
```

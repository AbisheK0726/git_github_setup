# Git & Github

## Git

Git is a version control system. It allows you to keep track of changes to your code. It also allows you to work on code with other people.

### Git Commands

- `git init` - initialize a git repository
- `git status` - check the status of your repository
- `git add` - add files to the staging area
- `git commit -m "message"` - commit changes to the repository, with a message
- `git log` - view the commit history
- `git push` - push changes to a remote repository
- `git pull` - pull changes from a remote repository
- `git clone` - clone a remote repository

Tip: You can use `git help <command>` to get more information about a command.

## Github

Github is a website that hosts git repositories. It allows you to share your code with other people, and collaborate on projects.
Github also has a lot of useful features, like issue tracking, pull requests, and code reviews.

### Github Commands

- `git remote add origin <url>` - add a remote repository
- `git push -u origin master` - push changes to the remote repository
- `git pull origin master` - pull changes from the remote repository

# An introduction to Python

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

## Task 1.3 - Input

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

## Task 1.4 - Operators

Operators are used to perform operations on variables and values.

### Arithmetic Operators

| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus | x % y |
| ** | Exponentiation | x ** y |
| // | Floor division | x // y |

### Assignment Operators

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

### Comparison Operators

| Operator | Name | Example |
| --- | --- | --- |
| == | Equal | x == y |
| != | Not equal | x != y |
| > | Greater than | x > y |
| < | Less than | x < y |
| >= | Greater than or equal to | x >= y |
| <= | Less than or equal to | x <= y |

### Logical Operators

| Operator | Description | Example |
| --- | --- | --- |
| and | Returns True if both statements are true | x < 5 and  x < 10 |
| or | Returns True if one of the statements is true | x < 5 or x < 4 |
| not | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

### Identity and Membership Operators

| Operator | Description | Example |
| --- | --- | --- |
| is | Returns True if both variables are the same object | x is y |
| is not | Returns True if both variables are not the same object | x is not y |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

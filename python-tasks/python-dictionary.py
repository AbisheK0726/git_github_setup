# Python Dictionary

# Store student information - name, course_name, progress, completed_lessons
# student = { "name": "John", 
#            "course_name": "Python", 
#            "progress": 50, 
#            "completed_lessons": 5 }

# # Print student information
# print(student)

# print(student["name"])
# print(student["course_name"])
# print(student["progress"])

"""
====================================================================================================
Task
"""

# Dictionary basics

#1 - Define a dictionary call story1, it should have the followign keys: 
#    'start', 'middle' and 'end'

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
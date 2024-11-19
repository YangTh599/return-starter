# Thayer Yang  
# 19 NOV 2024
# Return Statement Starter

# Destination in Euroasia

def describe_vacation(destination, activity, season="summer"):
    desc = f'I am vacating at {destination.title()} during {season}. I am {activity} in {destination.title()}'

    return desc

description1 = describe_vacation("Thailand", "hiking")
description2 = describe_vacation("Korea", "eating ricecakes", "spring")

for vacation in (description1, description2):
    print(vacation)

# Student Major

def show_major(first_name, university, major='Sports Medicine'):
    desc = f'{first_name.title()} attends {university.title()} and is majoring in {major.title()}'

    return desc

student1 = show_major("Spencer", "Michigan Institute of Technology", "Computer Science")
student2 = show_major("Joy", "Ferris State University")

for student in (student1,student2):
    print(student)

# None value returned

def what(magic):
    string = f"HEY {magic} ISNT ALLOWED HERE"

    return

print(what("lol"))
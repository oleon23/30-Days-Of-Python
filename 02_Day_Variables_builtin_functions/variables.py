
# Variables in Python

#Pre-text
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#     'firstname':'Asabeneh', 
#     'lastname':'Yetayeh', 
#     'country':'Finland',
#     'city':'Helsinki'
#     }

# # Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

# # Declaring multiple variables in one line

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

# #input
# first_name = input('What is your name?')
# age = input('How old are you?')
# print('Your name is', first_name, 'and you are', age, 'years old.')


#Day 2: 30 Days of Python programming
#Exercises L1
from math import pi


first_name = 'James'
last_name = 'Bond'
full_name = first_name + ' ' + last_name
country = 'Peru'
city = 'Lima'
age = 22
year = 2026
is_married = True
is_true = False
is_light_on = False

racing_team, championship_points, driver_name, driver_number, is_previous_world_champion = 'Mercedes AMG Pertronas', 173, 'George Russell', 63, False

#Exercises L2
variables = (first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on, racing_team, championship_points, driver_name, driver_number, is_previous_world_champion)
# for var in variables: 
#     print(type(var))

first_name_length = len(first_name)
last_name_length = len(last_name)
# if (first_name_length > last_name_length):
#     print('first name is longer')
# else: 
#     print('last name is longer')

num_one = 5
num_two = 4
total = num_one + num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor = num_one // num_two

# radius = 30
radius = int(input('Enter the radius:'))
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius
print('Radius: ' + str(radius) + '\n Area: ' + str(area_of_circle) + '\n Circumference: ' + str(circum_of_circle))

first_name = input('Enter a first name: ')
last_name = input('Enter a last name: ')
country = input('Enter a country: ')
age = input('Enter an age: ')
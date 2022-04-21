# Exercise 1
# Create a list named students containing some student names (strings).
students = ['Keziah', 'Joshua', 'Phillip', 'Jordan', 'Eric', 'Zoey', 'Mariah', 'Medinah', 'Noni','Ngozi', 'Journey', 'Malika', 'Anna']
# Print out the second student's name.
print(students[1])
# Print out the last student's name.
print(students[-1])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".
foods = ('pizza', 'veggie burger', 'cookies', 'chicken sandwich', 'fish taco', 'cupcake', 'ice cream', 'chicken fingers', 'turkey sandwich', 'calzone', 'tomato soup', 'greek salad', 'cheeseburger')
for food in foods:
    print(f'{food} is a good food')

# Exercise 3
# Using a for loop, print just the last two food strings from foods.
for food in foods[-2:]:
    print(food)

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
home_town = {
    'city': 'Atlanta',
    'state': 'GA',
    'population': 532695
    }
# Print a string with this format:
# "I was born in city, state - population of population"

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
for key, val in home_town.items():
    print (f"{key} = {val}")

# Exercise 6
# Create an empty list named cohort.
cohort =[]
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index]
    })
#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.
for student in cohort:
    print(student)

# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.
awesome_students = [f"{student} is awesome!" for student in students]
print(awesome_students)

# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
for food in [food for food in foods if 'a' in food]:
    print(food)
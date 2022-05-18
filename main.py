import requests
from sheety import Sheety
from nutritioniz import Nutritioniz

# Get rows, insert row on sheety
nutri = Nutritioniz()
sheety = Sheety()

# Get work out sentence
text = input("Whick exercises did you do? \n")

# Get synthesized work exercises
exercise_data = nutri.synthesize(text)

# Write workout excercises to workout googlesheet
for exercise in exercise_data["exercises"]:
    sheety.write_record(exercise)
            





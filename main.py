calorie_in = 2000
fat_in = 50
protien_in = 100
carbs_in = 50

total_calories = 0
total_fat = 0
total_protien = 0
total_carbs = 0

x = True

from nutr_charts import chickpeas
from nutr_charts import chickpeas2
from nutr_charts import burrito_bowl
from nutr_charts import crackers
from nutr_charts import apple
from nutr_charts import burger

while x is True:
    food_type = input("Enter what food you have ate today: ")
    if food_type == "chickpeas" or food_type == "CHICKPEAS":
        total_carbs = total_carbs + chickpeas.carbs
        total_fat = total_fat + chickpeas.fat
        total_protien = total_protien + chickpeas.protien
        total_calories = total_calories + chickpeas.calories

    elif food_type == "chickpeas2" or food_type == "CHICKPEAS2":
        total_carbs = total_carbs + chickpeas2.carbs
        total_fat = total_fat + chickpeas2.fat
        total_protien = total_protien + chickpeas2.protien
        total_calories = total_calories + chickpeas2.calories

    elif food_type == "burrito bowl" or food_type == "BURRITO BOWL":
        total_carbs = total_carbs + burrito_bowl.carbs
        total_fat = total_fat + burrito_bowl.fat
        total_protien = total_protien + burrito_bowl.protien
        total_calories = total_calories + burrito_bowl.calories

    elif food_type == "crackers" or food_type == "CRACKERS":
        total_carbs = total_carbs + crackers.carbs
        total_fat = total_fat + crackers.fat
        total_protien = total_protien + crackers.protien
        total_calories = total_calories + crackers.calories

    elif food_type == "apple" or food_type == "APPLE":
        total_carbs = total_carbs + apple.carbs
        total_fat = total_fat + apple.fat
        total_protien = total_protien + apple.protien
        total_calories = total_calories + apple.calories

    elif food_type == "burger" or food_type == "BURGER":
        total_carbs = total_carbs + burger.carbs
        total_fat = total_fat + burger.fat
        total_protien = total_protien + burger.protien
        total_calories = total_calories + burger.calories

    elif food_type == "x" or food_type == "X":
        x = False

print("Your total calories for today are : " + str(total_calories))
print("Your total protien intake for today is : " + str(total_protien))
print("Your total carbs for today are : " + str(total_carbs))
print("Your total fat intake for today is : " + str(total_fat) + "\n")




water_intake = 0
glass = 237
bottle = 500
x = True

recommended = int(input("Enter your reccomended water intake: "))

while x is True:
    water = input("Enter G for glass and B for bottle: ")
    if water == "g" or water == "G":
        water_intake = water_intake + 237
    elif water == "b" or water == "B":
        water_intake = water_intake + 500
    elif water == "x" or water == "X":
        x = False;

if water_intake >= recommended:
    print("\nGreat job! You have reached a required water intake of " + str(water_intake) + "mL.")

elif water_intake < recommended:
    required = recommended - water_intake
    print("\nUh oh, you only reached a water intake of " + str(water_intake) + "mL, you need " + str(required) + "mL more.")
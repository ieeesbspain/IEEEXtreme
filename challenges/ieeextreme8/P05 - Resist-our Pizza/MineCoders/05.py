# -*- coding: utf-8 -*-

base_calories=270

topping_calories = {
    'Anchovies' : 50,
    'Artichoke' : 60,
    'Bacon'     : 92,
    'Broccoli'  : 24,
    'Cheese'    : 80,
    'Chicken'   : 30,
    'Feta'      : 99,
    'Garlic'    : 8,
    'Ham'       : 46,
    'Jalapeno'  : 5,
    'Meatballs' : 120,
    'Mushrooms' : 11,
    'Olives'    : 25,
    'Onions'    : 11,
    'Pepperoni' : 80,
    'Peppers'   : 6,
    'Pineapple' : 21,
    'Ricotta'   : 108,
    'Sausage'   : 105,
    'Spinach'   : 18,
    'Tomatoes'  : 14
}

calories = 0

input_list = raw_input().split()

total_slices = int(input_list[0])

for n, top in zip(input_list[1::2], input_list[2::2]):
    calories += base_calories * int(n) # Sum calories for base piza
    
    toppings = top.split(",")
    for topping in toppings:
        calories += topping_calories[topping]*int(n) # Sum calories for topping
        
print "The total calorie intake is " + str(calories)
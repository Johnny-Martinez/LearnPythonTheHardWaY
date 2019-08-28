# Variable for my name
name = 'Johnny M'
# Variable for my age
age = 37
# Variable for my height
height = 68
# Variable for my weight
weight = 175
# Variable for my eyes
eyes = 'Brown'
# Variable for color of teeth
teeth = 'White'
# variable for color of hair
hair = 'Brown'

centimeters = height * 2.54
kilograms = weight * 2.205

print(f"Lets's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"and {centimeters} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"Which converts to {kilograms} Kilograms")
print(f"Actually, thats not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on coffee.")

# this line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get a {total}")

name = 'Cristian F. Moza'
age = 43 # not a lie.
height = 72 # inches
weight = 205 #lbs
eyes = 'brown'
teeth ='white/yellow'
hair = 'bold'

print(f"Let's talk about {name}.")
print(f"I am {height} inches tall.")
print(f"I am {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"I've got {eyes} eyes and {hair} hair.")
print (f"My teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

h_ft = 1
h_in = h_ft*12
h_cm = round(h_in*2.54, 1)

print (f"Height in Centimeters: {h_cm} cm")

print (f"Height in Inches: {h_in} in")

h_lbs = 1.0
h_kg = round(h_lbs* 0.4535, 2)
print (f"Kilogram Mass: {h_kg} kg")

types_of_people = 10 #count of types of people
x = f"There are {types_of_people} types of people." #variable defining
#the types_of_people

binary = 'binary' # string named 'binary'
do_not = "don't" # string named "don't"
y = f"Those who {binary} and those who {do_not}." #variable defining
#the 'binary' & "don't" strings (or variable - bad joke)

print(x) #printing variable defining the types_of_people (printing line 2)
print(y) #printing variable defining variable - bad joke (printing line 6)

print(f"I said: {x}") #re-printing variable defining the types_of_people adding
#& in front of the variable formated as string 'I said'(printing line 8)
print(f"I also said: {y}") #re-printing variable defining the bad joke variable
#& in front of the variable formated as string 'I also said'(printing line 9)

hilarious = False #variable hilarious defined as being false(untrue)
joke_evaluation = "Isn't that joke so funny?! {}" #variable called
#'joke_evaluation' formated as a string

print(joke_evaluation.format(hilarious)) #printing out the 'joke_evaluation'
#variable formated with .format() using variable 'hilarious'

w = "This is the left side of..." # defining variable 'w' as a string
e = "a string with a right side." # defining variable 'e' as a string

print(w + e) #adding the two variable defined above, var 'w' and var 'e' respectively.

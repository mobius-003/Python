# ex20: Functions and Files

# arg(s) = argument(s)
# var(s) = variable(s)
# fct(s) = function(s)

# Import argv vars from the sys module
from sys import argv

# Assign the 1st & 2nd args to the two vars
script, input_file = argv

# Defining 'print_all' func to print everything inside the input_file
# 'f' = variable name of the file
def print_all(f):
    #display the entire text
    print(f.read())
# Create a function to go at the begining of the file (i.e. byte 0-zero)
def rewind(f):
    f.seek(0)
# Create a function to print one line at the time ( 1, 2, & 3)
# line_count is the line number to be read; f is the name of the file
# readline is a buil-in function (method)
# display line by line inside the f file
def print_a_line(line_count, f):
    print(line_count, f.readline())

#open the input file (i.e ex20_txt.txt)
current_file = open(input_file)

#Display "First let's print the whole file:"" as separate line
print("First let's print the whole file:\n")

#print_all func to display the inside of the file
print_all(current_file)

#prints the string: "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

#call the rewind func to execute - the function will go to the begining of the file
rewind(current_file)

#Prints "Let's print three lines:"
print("Let's print three lines:")

#prints 3 lines (each line is associated with every sentence inside the input_file); Prints 1st sentence in the input file - func print_a_line
#set current line = 1
current_line = 1
print_a_line(current_line, current_file)

#set current line = 2 by adding 1 from Line 48
current_line += 1

#print line 2 by executing function print_a_line
print_a_line(current_line, current_file)

#Set current line = 3 by adding 1 from Line 52
current_line += 1

#print line 2 by executing function print_a_line
print_a_line(current_line, current_file)

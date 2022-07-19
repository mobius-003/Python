
# prints the sting in the double quotes "Let's practice everything."
print("Let's practice everything.")
# prints the sting  as follows:
# You 'd need to know 'bout escapes with \ that do:
# backslash character skips a space or the so called 'escape character'
# \\ double-backslash is a way of printing a simple backslash
# \n is for new line and one space
# \t creates a new tab (tab = 8 spaces - in Python) and a space
print('You \'d need to know \'bout escapes with \\ that do:')
print('\n newLines and \t tabs.')

# the poem var has triple qoutes
# it starts with a tab (\t) and a blank line
# \n create a new line and and an extra space
# another new line and two tabs ( a total of 16 spaces)
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# prints the var poem starting with ".........." and
# ending with "..............."
print("..........")
print(poem)
print("...............")

# prints the string 'This should be five: 5'; where 5 is the faviabe five
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# Creating a function which starts with start_point =10000
#calculates jelly_beans =10,000*500 = 5,000,000 beans
# calculates jars = 5,000,000/1000 = 5,000 jars
# calculates crates = 5,000 /100 = 50 crates
# return makes the values avialable but it doesn't print them.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
#These are the varaibles names WITHIN the function 'secret_formula'
#They are called local variables

#this var start_point is being used in line 41
#This call for a function and fills the three variable (global vars, not local vars)
# 'beans' is used instead of 'jelly_beans' but it doesn't matter. The vars
# can be called x, y and z, if we want. The funct just fills them in and
# returns values in the order that they were listed.

start_point =10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a string point of: {}".format(start_point))

# it's just like an f"" string
print(f"1. We'd have: {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10
# this is variation of the increment function:
# itereates the var 'start_point' and devides it by 10

#creates the initial variable to be used in the print line - Line 74
print(" We can also do that this way:")
formula = secret_formula(start_point)

# This is an easy way to apply a list to a format string
# This version calls on the function and fills the values directly
#without creating intermediate variable outsidethe function.
print ("2. We'd ALSO have: {} beans, {} jars, and {} crates.".format(*formula))


def break_words(stuff):
    """ THIS FUNCTION WILL BREAK UP WORDS FOR US. """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ Sorts the words for us. """
    return sorted(words)

def print_first_word(words):
    """ Prints the first words after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """ Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """ Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Instructions on how to run the script:

#1. Start Python: by typing python3.8

#2. Import this newly defined module
# >>> import ex25
#Note: don't type ".py" or an erro will be prompted.
#When you import this a new file will be created called "ex25.pyc"

#3. Creating an object to work with.
# >>>


#4. Run  1st function "break_words" and show results
# >>> words = ex25.break_words(sentence)
# >>> words

#5. Run 2nd function "sort_words" and show results
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words

#6. Run the 3rd function "print_first_word" (displays automatically)
#>>> ex25.print_first_word(words)

#7. Run the 4th function "print_last_word" (displays automatically)
#>>> ex25.print_last_word(words)

#8. Run the 5th function "sort_sentence" and show results
#>>> sorted_sentence = ex25.sort_sentence(sentence)
#>>> sorted_sentence

#9. Run the 6th function "print_first_and_last" (displays automatically)
#>>> ex25.print_first_and_last(sentence)

#10 Last function to be called "print_first_and_last_sorted" (displays automatically)
# >>> ex25.print_first_and_last_sorted(sentence)

#If you type help(ex25) you should get a block of text
#and the text in triple quotes for each function

#If you type help(ex25.break_words) you will see just trippled quted text for that function.

#Finally, you can avoid typing "ex25." at the beginning
#of everything if you import the module in this fashion:
# >>> from ex25 import *
# Then you can run the commands like this:
# Type ---> break_words(sentence) ....1st Function

#And quit Python3
#>>> quit()

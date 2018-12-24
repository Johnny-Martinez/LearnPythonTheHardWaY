#import argv library
from sys import argv
#set our variables for argv
script, filename = argv
#open text file... I called mine ex15_sample.txt
txt = open(filename)
#display output to the user: Here is your file(filename)
print "Here's your file %r:" % filename
#read the contents of the file.
print txt.read()

#ask user to input file for which they would like to read.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
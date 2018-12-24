from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#setup variables to copy data to and from
in_file = open(from_file)
indata = in_file.read()

#Tell the user how big the file is.
print "The input file is %d bytes long" % len(indata)

#Check to see if there is a new file to copy data to.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to aboart."

#Waiting on user input.
raw_input()

#opens the file to write the data to.
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alrighty... all done!"

#Closes both the input file and output file.
out_file.close()
in_file.close()

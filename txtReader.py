# per PEP8 style guide, imports on seperate lines
import os
import glob

# get pwd (working dir) and print. OS independent method.
# could be useful modules if attempting to search in other dirs or recursive search
pwd = glob.glob(os.getcwd())
print(pwd)


files = []
for file in glob.glob("*.txt"):
    files.append(file)
print(files)

#import fileinput (multiple streams) or use open() with loops to go into the txt files
#  fileinput looks more appropriate
#  need to get filenames and feed into a list for .input(arg).

import fileinput
x = fileinput.input(files)
print("\n# l# filename() isFirstLine")
print("*************************")
for line in x:
    print(x.fileno(), x.filelineno(), x.filename(), x.isfirstline())

print("\n")




## Files - printing contents only

#foreach filename, create file object with open
#foreach line in file (since file objects act as own iterator)
#print contents of line, uses rstrip to remove trailing whitespace & newline chars
#close the file and print a newline character to make it easier on the eyes to tell files apart
for fileName in files:
    f = open(fileName, "r")
    for line in f:
        print(line.rstrip())
    print("\n")
    f.close()
    
print("\n", f)

## Files continued - matching an input string
# get user input, verify string accepted, then test if s == line.rstrip()
# so far, no logic for telling which file the match resulted in, or which line of the file was a match

print("please enter the string you want to match \n")
s = input()
print(s, "accepted \n")

for fileName in files:
    f = open(fileName, "r")
    for line in f:
        print(s, line.rstrip())
        if s == line.rstrip():
            print("matched!", s)
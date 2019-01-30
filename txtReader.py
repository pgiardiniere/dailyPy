# per PEP8 style guide, imports on seperate lines
import os
import glob

# get pwd (working dir) and print. OS independent method.
# could be useful modules if attempting to search in other dirs or recursive search
pwd = glob.glob(os.getcwd())
print(pwd)

s = input("enter string to query txt files in current directory for")

#foreach file in pwd 
#  print contents --- expand to actually take s and search each file for it.
for file in glob.glob("*.txt"):
  print(file)

#import fileinput (multiple streams) or use open() with loops to go into the txt files
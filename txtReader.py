import glob
import fileinput
import re

# get all .txt files in current dir and add them to the list files
files = []
for file in glob.glob("*.txt"):
    files.append(file)
print("\nThe files are:\n", files)

#get string to match:
print("please enter the string you want to match \n")
s = input().strip().lower()
print(s, "accepted \n")

# documentation https://docs.python.org/2/library/fileinput.html
# iterates line-by-line thru each file in the files list, evaluates whole-line string match (less newline)

fi = fileinput.input(files)
for line in fi:
    if (line.lower().find(s) > -1): 
        print("Match found in: {0}, line number {1}.".format(fi.filename(), fi.filelineno()))
        print("The line reads: {0}".format(line))



import glob
import fileinput
import re

###############
### TO-DO
# when working in tech txt notes dir, the output is SUPER long as it prints absolute path of entire txt file. Need to truncate
# can either 1) cut the output from the strings somehow, 
# or 2) do something to 'switch' execution actually into that dir and then execute
# 
# that would reduce redundant code - i.e. it would work the same in pwd or in another remote dir
# also opens up the possibility for arbitrary dir search
###############

# confirm user is searching the standard tech txt notes dir
print("Hit enter to search your standard tech txt notes dir. Insert any string to search current dir instead\n")
pwd = input()

# if Return inputted, get all .txt files in tech txt notes dir and add them to the list files. Else, just use current dir
if pwd == '':
    files = []
    for file in glob.glob(r"C:\\Users\\Pete\\Google Drive\\Tech txt notes\\*.txt"):
        files.append(file)
    print("\nThe files are:\n", files)
else:
    files = []
    for file in glob.glob("*.txt"):
        files.append(file)
    print("\nThe files are:\n", files)

#get string to match:
print("please enter the string you want to match\n")
s = input().strip().lower()
print(s, "accepted \n")

# documentation https://docs.python.org/2/library/fileinput.html
# iterates line-by-line thru each file in the files list, evaluates whole-line string match (less newline)

fi = fileinput.input(files)
for line in fi:
    if (line.lower().find(s) > -1): 
        print("Match found in: {0}, line number {1}.".format(fi.filename(), fi.filelineno()))
        print("The line reads: {0}".format(line))



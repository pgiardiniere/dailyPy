from glob import glob
import fileinput
import os

###############
### TO-DO
#
###############


# confirm user is searching the standard tech txt notes dir
print("Hit enter to search your standard tech txt notes dir. If you'd like to search another dir, enter the abs/rel path\n")
pwd = input()

# if Return inputted, move to Tech txt notes dir. Otherwise, current directory is queried.
if pwd == '':
    os.chdir("/Users/Pete/Google Drive/Tech txt notes")
else:
    os.chdir(pwd)

files = []
for file in glob("*.txt"):
    files.append(file)
print("The files are:\n####################")
for file in files:
    print(file)

#get string to match:
print("\nplease enter the string you want to match\n")
s = input().strip().lower()
print(s, "accepted \n")

# documentation https://docs.python.org/2/library/fileinput.html
# iterates line-by-line thru each file in the files list, evaluates whole-line string match (less newline)

fi = fileinput.input(files)
for line in fi:
    if (line.lower().find(s) > -1): 
        print("Match found in: {0}, line number {1}.".format(fi.filename(), fi.filelineno()))
        print("The line reads: {0}".format(line))



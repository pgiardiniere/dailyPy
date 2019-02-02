# get all .txt files in current dir and add them to the list files
import glob
files = []
for file in glob.glob("*.txt"):
    files.append(file)
print("\nThe files are:\n", files)

#get string to match:
print("please enter the string you want to match \n")
s = input()
print(s, "accepted \n")

# documentation https://docs.python.org/2/library/fileinput.html
# iterates line-by-line thru each file in the files list, evaluates whole-line string match (less newline, obv)
#   need fileinput assigned to variable fi in order to access
#       isn't there a 'this' or 'self' method of self-referncing an objects. might use Super? not sure. revisit.
import fileinput
fi = fileinput.input(files)
for line in fi:
    print(s, line.rstrip())
    if (s == line.rstrip()): print("\t\t MATCH FOUND IN", fi.filename() + ",", "line", fi.filelineno())

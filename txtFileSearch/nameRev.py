import fileinput
import os

os.chdir("/Users/PG053982/Downloads")
print(os.getcwd())

fi = fileinput.input("lastFirstNames.csv")
for line in fi:
    s = line.split(",")
    sLast = s[0].strip().strip('"')
    sFirst = s[1].strip().strip('"')
    print(sFirst, sLast)

# don't need to save to an output file, just run in iPython and paste back into the excel sheet we're working from for properly formatted data
# per PEP8 style guide, imports on seperate lines
import os
import glob

pwd = glob.glob(os.getcwd())

for file in glob.glob("*.txt"):
  print(file)

print(pwd)
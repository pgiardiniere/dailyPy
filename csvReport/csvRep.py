# Creates graph from given CSV file input

# imports
import os
from glob import glob
import fileinput
import matplotlib as plt

# take user input for dir to search for CSVs
print("enter the directory (unix or win-double bckslash if win style) containing files to search")
os.chdir(input())

print(os.getcwd())
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the 'true' len of str.
import numpy as np


# String function
def make_url(s):
    L = s.split(' ')
    print(L)
    s = ''
    for i, w in enumerate(L):
        s += w
        s += '%20' if i != len(L)-1 else ''
    return s


# List function
def make_url_from_list(L):
    for i, c in enumerate(L):
        if c == ' ':
            L[i] = '%20'
    return L


# NP char array function
def make_url_from_arr(L):
    for i, c in enumerate(L):
        if i == 0:
            L2 = np.array(c)
        elif c == ' ':
            L2 = np.append(L2, ['%', '2', '0'])  # can also do '%20'
        else:
            L2 = np.append(L2, c)
    return L2


# URL-ify a string.
s = 'one space'
print(s)
s = make_url(s)
print(s, end='\n\n')


# URL-ify a Python List
s = 'one space'
L = []
for i, c in enumerate(s):
    L.append(c)

print(L)
L = make_url_from_list(L)
print(L, end='\n\n')


# URL-ify a NumPy char array.
s = 'one space'
for i, c in enumerate(s):
    if i == 0:
        L = np.array(c)
    else:
        L = np.append(L, c)


print(L)
L = make_url_from_arr(L)
print(L, end='\n\n')

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


# NP char array function. Still not in-place.
def make_url_from_arr(L):
    for i, c in enumerate(L):
        if i == 0:
            L2 = np.array(c)
        elif c == ' ':
            L2 = np.append(L2, ['%', '2', '0'])  # can also do '%20'
        else:
            L2 = np.append(L2, c)
    return L2


# NP char array function, in-place. Pass in some padded array
def make_url_in_place(L):
    count = 0
    for i, c in enumerate(L):
        if c == ' ':
            count += 1
    i_adj = count * 3

    i = L.size - 1
    j = i - i_adj
    while (j > -1):
        if L[j] == ' ':
            L[i] = '0'
            L[i-1] = '2'
            L[i-2] = '%'
            i -= 2
        else:
            L[i] = L[j]
        i -= 1
        j -= 1
    return L


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


# URL-ify a NumPy char array in-place
s = 'one space'
for i, c in enumerate(s):
    L = np.array(c) if i == 0 else np.append(L, c)
L = np.append(L, ['0', '0', '0'])

print(L)
L = make_url_in_place(L)
print(L, end='\n\n')



# Hint #1:
"""
It's often easiest to work with strings from back to front.
"""

# Hint #2:
"""
You might find you need to know num spaces. Try just counting them.
"""

# Screw it, let's do this in Java real quick.
# Alright, that was not the best idea.

# Figure out how NumPy does in-place reassignment of array size...

# AH HAH
# https://numpy.org/devdocs/user/whatisnumpy.html

# NumPy arrays are fixed in size at their creation.
# If you need more elemenents than were in the original array,
# you'll have to create a new array and put the stuff in there.

# Oh wait.
# If you're reallocating an array in C/Java, you're doing the same thing.

#   define array : len(arrray) = 2 * length of old array
#   iterate through old array, copying elements in to new
#   use the additional space for extra stuffs.

# So I guess we're meant to assume that the array is padded with nulls / 0s

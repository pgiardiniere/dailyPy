# Question 1.1 in Cracking the Coding Interview:
# Implement an algorithm to determine if a string has all unique characters.
# What if you can't use additional data structures?

s1 = 'hello'
s2 = 'hi'


# The Python way
def is_unique(s):
    for i, ci in enumerate(s):
        for j, cj in enumerate(s):
            if ci == cj and i != j:
                return False
    return True


# The 'normal' way
def is_unique_2(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                return False
    return True


is_unique(s1)
is_unique(s2)

is_unique_2(s1)
is_unique_2(s2)

# This algorithm is O(n^2) temporal complexity,
# as we have singly nested loop of n elements.

# This algorithm is O(n) spacial complexity,
# as we require a single string (array) of n elements.


# ------------------------------
# hint #1: "Try a hash table."

# Oh, sure. With a hash table, you hash the alphabet
# (or the entire ascii/UTF-8 character set).

# Yields O(n+m) complexity, for n: size of string,
# and m: size of character set

# Wait... no it's not that either. You just hash each character.
# Then if you have any collisions, instead of chaining/linear probing,
# you simply return False.

# Yields O(n) complexity for n: size of string.


# I haven't hashed in Python before, just java. See following for starters:
# https://www2.cs.arizona.edu/classes/cs210/fall17/lectures/hashmap.pdf
# http://zetcode.com/python/hashing/


# So, to implement. I can either make a dictionary with hashcode:char,
# or make a set of hashcodes. 

# I feel like I'd prefer just the set in this case.


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


# Less Pythonic way
def is_unique_2(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                return False
    return True


# Non-Pythonic way. Just don't even do this.
def is_unique_3(s):
    i, j = 0, 0
    while i < len(s):
        while j < len(s):
            if s[i] == s[j] and i != j:
                return False
            j += 1
        i += 1
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

# I feel like I'd prefer just the set in this case. Let's do both.

def set_hash_unique(s):
    hashes = set()
    for c in s:
        hashes.add(hash(c))
    if len(hashes) < len(s):
        return False
    return True


def dict_hash_unique(s):
    d = {}
    for c in s:
        d[c] = hash(c)
    if len(d) < len(s):
        return False
    return True


set_hash_unique(s1)
set_hash_unique(s2)

dict_hash_unique(s1)
dict_hash_unique(s2)

# This algorithm is O(n) time complexity.


# ------------------------------
# hint #2: "Could a bit vector be useful?" (#111)

# well ... the bits of each char a string would also map to unique bitstrings
# the entire string itself would map to a unique bitstring

# I don't see any performance improvement above O(n) though...


# ------------------------------
# hint #3:  "Could you solve it in O(n log n) time?"
#           "What might a solution look like?"      (#132)

# O(n log n) implies we are sorting the data using with QuickSort
# (or a similar time-complexity sort algo)

# A linear pass to check duplicates would add an additional O(n) algo

# We have sort: some f1 that's O(N log N) and linear pass: f2 that's O(N),
# Then sort + linear pass is O(max(f1, f2))
# = O(max(n, n log n))
# = O(n log n).

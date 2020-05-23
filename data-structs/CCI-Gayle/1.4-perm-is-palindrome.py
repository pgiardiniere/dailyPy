# Palindrome Permutation: Given a string, write a function to check
# if it is a permutation of a palindrome.

# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.

# The palindrome does not need to be limited to just dictionary words.

# Example:
# Input: Tact Coa
# Output: True (perms: taco cat, atco cta)
# Hints: 106, 121, 134, 136


def is_palindrome(s):
    s = ''.join(s.split(' '))  # Remove spaces from string
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# Test is_palindrome:
s = 'nurses run'
print(is_palindrome(s))
s = 'garbage'
print(is_palindrome(s))


# Sort solution: If we're not within 1 character of mirror, can't have pal.
#   Temporal Complexity: O(N log N)   due to sort()
#   Spatial Complexity: O(1)          due to sort() in-place
def has_palindrome(s):
    s = ''.join(s.split(' ')).lower()
    s = sorted(s)

    no_pair = 0
    i = 0
    while (i < len(s) - 1):
        if s[i] == s[i + 1]:
            i += 2
        else:
            no_pair += 1
            i += 1

    if no_pair > 1:
        return False
    else:
        return True


# Test has_palindrome:
s = 'nurses run'
print(has_palindrome(s))
s = 'garbage'
print(has_palindrome(s), end='\n\n')


# Hash-table solution:
#   Temporal Complexity: O(N)
#   Spatial Complexity: O(N)
import numpy as np  # noqa


def map_unicode_int(c):
    a = ord('a')
    z = ord('z')
    if (a <= ord(c) <= z):
        return ord(c) - a
    return -1

def hashmap_has_palindrome(s):  # noqa
    s = ''.join(s.split(' ')).lower()
    hm = np.zeros(26)

    # Create a hashmap of num occurrences of lowercase alpha chars
    for i, c in enumerate(s):
        dest = map_unicode_int(c)
        hm[dest] += 1

    print(hm)

    num_odds = 0
    for i in range(hm.size):
        if hm[i] % 2 != 0:
            num_odds += 1

    return True if num_odds <= 1 else False


# Test has_palindrome:
s = 'nurses run'
print(hashmap_has_palindrome(s))
s = 'garbage'
print(hashmap_has_palindrome(s), end='\n\n')


# I believe this solves the problem as it was formulated.
# No need to generate what those perms acutally are, but if I wanted to...

# It'd essentially be the same method as my is_palidrome check,
# except it constructs a string in that manner.


# Brute force: Generate all permutations, feed one at a time to is_palindrome()
# Time complexity: O(N!)


# Hints:
# 106
"""You don't have to (and shouldn't) gen all permutations.
That'd be inefficient.
"""

# 121
"""
What characteristics would a string that is a permutation of a palindrome have?
"""

# 134
"""Have you tried a hash table? You should get this to O(n) time.
"""

# Recall Big-O times, definition of hashmap data structure:
# https://www.bigocheatsheet.com/
# https://en.wikipedia.org/wiki/Hash_table

# Oh, duh.
# Python dictionaries are a particular implementation of a hash table
# But if we want to be able to define linear probing behavior (and access them)
# ourselves, we have to roll our own table.
# I'll do that with a simple List


# 136
"""Can you reduce space usage through a bit vector?
"""

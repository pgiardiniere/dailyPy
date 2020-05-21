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


# Check: If we're not within 1 character of mirror, we cannot have palindrome.
# Sort: O(N log N)
def has_palindrome(s):
    s = ''.join(s.split(' '))
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
print(has_palindrome(s))


# I believe this solves the problem as it was formulated.
# No need to generate what those perms acutally are, but if I wanted to...

# It'd essentially be the same method as my is_palidrome check,
# except it constructs a string in that manner.


# Brute force: Generate all permutations, feed one at a time to is_palindrome()
# Time complexity: O(N!)

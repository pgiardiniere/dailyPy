# Given two strings: write a function to decide if one is perm of other.


# Determine whether s2 is a permutation of s1.
# We have O(n^2) time complexity. O(n) space complexity.
def is_permutation(s1, s2):
    if len(s2) > len(s1):
        return False

    for c2 in s2:
        if c2 not in s1:
            return False

    return True


# def is_strict_permutation(s1, s2):
    


if __name__ == '__main__':
    s1 = 'hello'
    s2 = 'leo'
    print(is_permutation(s1, s2))

    # Wait, is_permutation is just checking whether or not we have arrangement
    # strictly speaking, a permutation would be the same length.

    """
    Hint 1:
    Describe what it means for two strings to be permutations of each other.
    Now, look at that definition you provided.
    Can you check the strings against that definition?
    """

    # Yeah, as I thought. Playing with definition.

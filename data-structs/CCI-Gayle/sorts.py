def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# Quadratic sort - i.e. O(N^2)). Worse than insertion sort. Better than bubble.
def selection_sort(L):
    for i in range(len(L) - 1):
        min_ind = i
        for j in range(i+1, len(L)):
            if L[j] < L[min_ind]:
                min_ind = j
        if min_ind != i:
            swap(L, i, min_ind)


# Quadratic sort. O(N^2) complexity.
def insertion_sort(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j-1] > L[j]:
            swap(L, j-1, j)
            j -= 1


# O(n log n) complexity in average case. O(n^2) worst case (pre-sorted list).
def quicksort(L, low, high):
    if low < high:
        piv_ind = partition(L, low, high)
        quicksort(L, low, piv_ind - 1)
        quicksort(L, piv_ind, high)


# Use Lomuto partitioning for simplicity of implementation.
def partition(L, low, high):
    pivot = (L[high])
    i = low
    for j in range(low, high):
        if L[j] < pivot:
            swap(L, i, j)
            i += 1
    swap(L, i, high)
    return i

# Merge Sort, Heap Sort, would both be O(N log N) sorts I could also add
# But Quicksort (with optimizations) is faster than them.

# As it stands, the version of Quicksort I implemented has worst-case runtime
# of O(N^2), which occurs when run upon a pre-sorted array.

# Easy optimization would be:
# Pick pivot index as median of the first, middle and last elements:

# if (a < b < c) or (c < b < a):
#     return b
# if (b < a < c) or (c < a < b):
#     return a
# else:
#     return c

# Other optimizations would be:
# Spatial optimization of O(log N)  (also better than counterparts merge/heapsort)
# recur first into smaller side of partition, using tail recursion into larger

# This ensures when you finish sorting smaller partition, you iterate through
# the entirety of larger partition.


# Test all sort methods:
if __name__ == '__main__':

    print('Insertion sort:')
    L1 = ['bc', 'ab', 'aa']
    print(L1)
    insertion_sort(L1)
    print(L1, end='\n\n')

    print('Selection sort:')
    L1 = ['bc', 'ab', 'aa']
    print(L1)
    selection_sort(L1)
    print(L1, end='\n\n')

    print('Quicksort:')
    L1 = ['bc', 'ab', 'aa']
    print(L1)
    quicksort(L1, 0, len(L1)-1)
    print(L1, end='\n\n')

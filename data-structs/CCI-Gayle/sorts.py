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


# Quadtratic sort. O(N^2) complexity.
def insertion_sort(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j-1] > L[j]:
            swap(L, j-1, j)
            j -= 1


# O(n log n) complexity.
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

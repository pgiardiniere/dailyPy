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
def quick_sort(L):
    print('sorted lel')


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

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

# Quadratic (i.e. O(N^2)) sort. Worse than insertion sort. Better than bubble.


def insertion_sort(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j-1] > L[j]:
            swap(L, j-1, j)
            j -= 1
    return L


if __name__ == '__main__':
    # Test all sort methods:
    print('Insertion sort:')
    L1 = ['bc', 'ab', 'aa']
    print(L1)
    insertion_sort(L1)
    print(L1, end='\n\n')

    print('Selection sort:')

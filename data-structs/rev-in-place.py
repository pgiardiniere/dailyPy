# In-place list reverse: std lib
L = ['a', 'b', 'c']
L.reverse()
print(L)

L = [1, 2, 3, 4, 5]
i = len(L) - 1
j = 0
while i > j:
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
    i -= 1
    j += 1
print(L)

def reversNumber(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1


# a = [1, 2, 3, 4, 5, 6]
a = [6, 5, 4, 3, 2, 1]
print(a)
reversNumber(a, 0, 5)
print("The revers array is: ")
print(a)



# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is , n = mi for some
# integer i, and False otherwise


def is_multiple(n, m):
    i = n % m
    if (i == 0):
        return True
    if (i != 0):
        return False


a = input("Enter two numbers,multiplt of \'a\' and \'a\' separated by space")
b = a.split()
print(is_multiple(int(b[0]), int(b[1])))

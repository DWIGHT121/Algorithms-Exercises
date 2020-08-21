# Draw the recursion trace for the computation of power(2,18), using the
# repeated squaring algorithm.

print("This is a program to print the power of certain integer using recursion method")


def power_value(base, power):
    if power == 1:
        return base

    else:
        return base*power_value(base, power-1)


base = int(input("Enter the base value"))
poww = int(input("Enter the power value"))

print(power_value(base, poww))

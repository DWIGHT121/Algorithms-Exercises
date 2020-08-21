# Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type

class Flower():
    def __init__(self, name, num_of_petals, price):
        self.name = name
        self.num_of_petals = num_of_petals
        self.price = price

    def get_name(self):
        return self.name

    def get_num_of_petals(self):
        return self.num_of_petals

    def get_price(self):
        return self.price


a = Flower("Lily", 20, 100.50)
print(a.get_name())
print(a.get_price())
print(a.get_num_of_petals())

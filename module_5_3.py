class House():
    def __init__(self, name, namber_of_floors):
        self.name = name
        self.namber_of_floors = namber_of_floors
    def __len__(self):
        return self.namber_of_floors
    def __str__(self):
        return 'Название '+self.name+', количество этажей '+str(self.namber_of_floors)
    def __eq__(self, other):
        if isinstance(other,House):
            return self.namber_of_floors == other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors == other.namber_of_floors
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if isinstance(other,House):
            return self.namber_of_floors < other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors < other
    def __le__(self, other):
        if isinstance(other, House):
            return self.namber_of_floors <= other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors <= other
    def __gt__(self, other):
        if isinstance(other, House):
            return self.namber_of_floors > other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors > other
    def __ge__(self, other):
        if isinstance(other, House):
            return self.namber_of_floors >= other.namber_of_floors
        elif isinstance(other, int):
            return self.namber_of_floors >= other
    def __add__(self, other):
        if isinstance(other, House):
            self.namber_of_floors += other.namber_of_floors
        elif isinstance(other, int):
            self.namber_of_floors += other
        return self
    def __iadd__(self, other):
        return self.__add__(other)
    def __radd__(self, other):
        return self.__add__(other)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__


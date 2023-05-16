#First class Coffe Cup
# capacity (how much coffee can it hold)
# amount (how much is it currently holding)
# fill (to fill the cup to it's max capacity with coffee)
# empty (to rid the cup of any existing coffee by drinking it all or pouring it out)
# drink (to drink some amount of the coffee that is currently in the cup)

    # each class needs a constructor, just like in js
    # in python, we use a specific function as the constructor
    # this constructor is a double-under(AKA dunder method)
    # these methods are built into python(typically as class)
    # these dunder methods all do specific things for us
    # the __init__ method, ALWAYS takes the keyword `self` as the first parameter
    # self is the keyword that we use to get each class to refer to the object it has created(or will create). 
    # just like `this` in js
class CoffeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0
    def __str__(self):
        return f"this {self.capacity}oz cup is full {self.amount}oz full"
    def fill(self):
        print('pouring coffee into the cup...')
        self.amount = self.capacity
        print(self)
    def empty(self):
        print('emptying the cup...')
        self.amount = 0
        print(self)
    def drink(self, sip):
        print(f'drinking {sip}oz of coffee...')
        self.amount-= sip
        if (self.amount <= 0):
            self.amount = 0
        print(self)

#create an instance (object) by calling the class and save the result to a variable
alexs_cup = CoffeCup(24)
finns_cup = CoffeCup(16)

# alexs_cup.fill()
# alexs_cup.drink(28)
# alexs_cup.empty()

import math


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"coordinates: ({self.x}, {self.y})"

    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    # def distance_to_origin(self):
    #     return (self.x ** 2 + self.y ** 2) ** .5
   
    def distance_to_point(self, point2):
        # to get the dist between two points we need two things first
        # distance between x coords
        dx = self.x - point2.x
        # distance between y coords
        dy = self.y - point2.y
        # basically, a^2 + b^2 = c^2, and to get the actual distance,
        # we are calculating the square root of c^2(which gives us c)
        return math.sqrt(dx ** 2 + dy ** 2)

# if we want to add to the class after definition, we can
Point.ORIGIN = Point()

point_one = Point()
point_two = Point(3, 4)
point_three = Point(6, 13)
point_four = Point(1, 1)
point_five = 'timm is hungry for lunch already'

# print(point_one)
# print(point_one.ORIGIN)
# print(point_one.distance_to_origin())
print(point_two)
# print(point_two.distance_to_origin())
print('distance between point_one and point_two')
print(point_two.distance_to_point(Point.ORIGIN))
# print('distance between point_three and point_four')
# print(point_three.distance_to_point(point_four))
# you can also instantiate objects from a class without saving to a variable
# print(point_three.distance_to_point(Point(2, 5)))
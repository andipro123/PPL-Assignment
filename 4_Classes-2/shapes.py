from abc import ABC, abstractmethod
from math import sqrt
#Base class
class Shapes:
    def __init__(self):
        self._Type = '' #Protected member
        print("A shape has been created!")

    def get_Type(self):
        print(self._Type)
        
    def __del__(self):
        print('Shape has been destructed!')
        
    @abstractmethod    
    def get_area(self):
        pass
        
#Triangle
class triangle(Shapes):
    def __init__(self):
        self._side = 3
    #We can modify protected members via base class    
    def set_type(self):
        self._Type = 'Polygon with 3 sides'
    #Only member functions can have access to private members    
    def get_side(self):
        print(self._side)
        
#Equilateral traingle inherited from triangle
class equilateral(triangle):
    def __init__(self, length):
        self.__length = length
    #We can modify protected members via base class    
    def set_type(self):
        self._Type = 'Polygon with 3 sides and all three are equal'
    #Only member functions can have access to private members    
    def get_side(self):
        print(self._side)
        
    #We use polymorphism to override the abstract method of the interface.
    
    def get_area(self):
        print((sqrt(3) / 4) * (self.__length ** 2))
        
#Rectangle
class rectangle(Shapes):
    def __init__(self):
        self.__side = 4
    #We can modify protected members via base class    
    def set_type(self,typ):
        self._Type = 'Polygon with 2 equal and 2 unequal sides'
    #Only member functions can have access to private members    
    def get_side(self):
        print(self.__side)
        
#Square inherited from rectangle
class square(rectangle):
    def __init__(self):
        self.sides = 4
    #We can modify protected members via base class    
    def set_type(self):
        self._Type = 'Polygon with 4 sides all of which are equal'
    
    def get_side(self):
    #The getter function will throw an error if this is executed as the private member of base class is being accessed
    #print(self.__side)
        print(self.sides)
        
#Rhombus inherited from square
class rhombus(square):
    def set_type(self):
        self._Type = 'Polygon with 4 sides all of which are equal but angles are not 90'
    
    #The base class has a public member in sides so we can access it in the base class and outside
    def get_side(self):
        print(self.sides)
        
#Circle
class circle(Shapes):
    def __init__(self):
        Shapes.__init__(self)
        self.__r = 0
        self.__eqn = 'x^2 + y^2 = r^2'
    def set_type(self):
        self._Type = 'Conic'
    #Setter function for accessing private member
    def set_radius(self,r):
        self.__r = r
    def get_area(self):
        print(3.14 * (self.__r)**2)
        
#Ellipse
class ellipse(Shapes):
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__eqn = 'x^2/a^2 + y^2/b^2 = 1'
    def set_type(self):
        self._Type = 'Conic with a major and minor axis'
    #Setter function for accessing private member
    def set_radius(self,a,b):
        self.__a = a
        self.__b = b
    def get_area(self):
        print(3.14 * self.__a * self__b)

if __name__ == "__main__":
    pass
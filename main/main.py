
from abc import ABC, abstractmethod

#from decorators import MiClase

class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1
 
    @classmethod # @staticmethod , no recibe el (cls)
    def RobotInstances(cls):
        # cls.__counter += 1
        return Robot.__counter

    @property # METODOS GET
    def x(self):
        return self.__x

    @x.setter # METODOS SET: @zeta.setter
    def x(self, x):
        self.__x = x

class AbstractClassExample(ABC): 
    def __init__(self, value): 
        self.value = value
        super().__init__() 
    
    @abstractmethod
    def do_something(self): 
        pass

class Bird:
    def __init__(self, species):
        self.__species = species
    def fly(self):
        print( self.__species + ' FLIES !!')

class Duck(Bird):
    def __init__(self):
        super().__init__('DUCK')

if (__name__ == "__main__"):
    nat = Robot()
    nat.x = 40
    ## EJEMPLOS DE USO ERRONEOS: nat.x(4), nat.x()
    print( nat.x )

    #rt = MiClase('alelimo')
    #print(rt.nombre)
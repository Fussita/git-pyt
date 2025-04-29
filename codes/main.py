

class Robot:
    __x = 4
    name = 'nona'

    def __init__(self, name):
        print('HOLA')
        self.name = name

    @classmethod
    def robotInstances(cls):
        print('44')    
    
    @staticmethod
    def RobotInstances():
        return Robot.__X

    # GET
    @property
    def x(self):
        return self.__X

    # SET
    @x.setter
    def x(self, x):
        self.__x = x

x = Robot("name")

Robot.robotInstances()

class Machine(Robot):
    z = 44
    def __init__(self, name, z):
        super().__init__(name)
        self.z = z
y = Machine('asd', 80)

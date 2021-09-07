class Vehicle:
    pass


class OnSurfaceVehicle:
    def __init__(self, brand1):
        self.brand1 = brand1

    @staticmethod
    def forward():
        return "forward"

    @staticmethod
    def backward():
        return "backward"

    @staticmethod
    def right():
        return "right"

    @staticmethod
    def left():
        return "left"


class InSpaceVehicle:
    def __init__(self, brand2):
        self.brand2 = brand2

    @staticmethod
    def up():
        return "up"

    @staticmethod
    def down():
        return "down"

    @staticmethod
    def takeoff():
        return "takeoff"

    @staticmethod
    def landing():
        return "landing"


class UnderWaterVehicle:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def immerse():
        return "go underwater"

    @staticmethod
    def surfacing():
        return "surfacing"


class Aircraft(OnSurfaceVehicle, InSpaceVehicle):
    def __init__(self, brand1, brand2):
        OnSurfaceVehicle.__init__(self, brand1)
        InSpaceVehicle.__init__(self, brand2)


class Submarine(OnSurfaceVehicle, InSpaceVehicle, UnderWaterVehicle):
    def __init__(self, brand1, brand2, model):
        OnSurfaceVehicle.__init__(self, brand1)
        UnderWaterVehicle.__init__(self, model)
        InSpaceVehicle.__init__(self, brand2)


ac = Aircraft(brand1='Boeing', brand2='777')
print("Aircraft can fly", ac.up(), '.')
print("Aircraft can fly", ac.forward(), '.')
print("Aircraft can", ac.takeoff(), '.')
print("Aircraft can fly", ac.right(), '.')
print(' * ' * 10)
sm = Submarine(brand1='USS George Washington', brand2='SSBN', model='598')
print('Submarine can', sm.immerse())
print('Submarine can sail', sm.down())
print('Submarine can', sm.surfacing())
print('Submarine can sail', sm.right())
print(' = ' * 10)
print(Aircraft.__mro__)
'''<class '__main__.Aircraft'>, <class '__main__.OnSurfaceVehicle'>, 
<class '__main__.InSpaceVehicle'>, <class 'object'>)
Класс Aircraft наследует свои свойства из класса OnSurfaceVehicle, так как самолёт может совершать все манёвры, 
свойственные наземному транспорту, когда он на земле. После взлёта он может совершать дополнительно и манёвры,
возможные в трёхмерном пространстве, как в классе InSpaceVehicle. И, в конечном итоге все эти классы являются наслед-
никами прародительского главного класса "object"'''
print(Submarine.__mro__)
'''(<class '__main__.Submarine'>, <class '__main__.OnSurfaceVehicle'>, 
<class '__main__.InSpaceVehicle'>, <class '__main__.UnderWaterVehicle'>, <class 'object'>)
Класс Submarine наследует свои свойства из класса OnSurfaceVehicle, так как подводная лодка может совершать все манёвры, 
свойственные транспорту на поверхности воды, когда она в режиме всплытия . Кроме того подводная лодка может совершать
дополнительные манёвры, свойственные подводным аппаратам в трёхмерном пространстве глубин, класс InSpaceVehicle. 
Особые свойства она черпает из класса UnderWaterVehicle, описывающие её свойства при переходе из/в режима всплытия 
в режим подводного плавания. И, в конечном итоге, все эти классы являются наследниками прародительского 
главного класса "object"'''

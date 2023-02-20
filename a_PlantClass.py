#superclass
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):    
        return self.__color

#subclass
class Flower(Plant):   #Plant superclass, it is in the ()
    def __init__(self,color, petals):
        Plant.__init__(self,color)  #creates a plant with color

        self.__petals = petals      #petals apply only to flowers

    def get_petals(self):
        return self.__petals

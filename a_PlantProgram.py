import a_PlantClass as pc

primrose = pc.Plant("Green")    #instance of superclass plant Green

sunflower = pc.Flower("Yellow",12) #instnce of Subclass  # needs a number of petals

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


print(primrose.get_petals())

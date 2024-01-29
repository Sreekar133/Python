class kettle(object):
    power_source = "electricity"
    def __init__(self,make,price):
        self.make=make
        self.price =price
        self.on=False

    def switch_on(self):
        self.on = True

kenwood = kettle("Kenwood",8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = kettle("Hamilton",14.55)
print(hamilton.make)
print(hamilton.price)

print("Models : {} = {} , {} = {}".format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))

print("Models : {0.make} = {0.price} , {1.make} = {1.price}".format(kenwood,hamilton))

print(hamilton.on)
print(hamilton.switch_on())

kettle.switch_on(kenwood)
print(kenwood.on)

kettle.switch_on(hamilton)
print(hamilton.on)

print("*" * 90)

kenwood.power = 1.5
print(kenwood.power)
print("switch to atomic source")
kettle.power_source = "atomic"
print(kettle.power_source)
print("switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)

print(kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)


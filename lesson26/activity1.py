class Vehicle :
    def __init__(self,name, max_speed, milage):
        self.name = name
        self.max_speed= max_speed
        self.milage = milage


class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 180, 12)
print("vehicle name:",School_Bus.name,"speed",School_Bus.max_speed,"milage:",School_Bus.milage)
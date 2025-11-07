class Vehicle:

    def _init_(self, max_speed, mileage):
      self.max_speed = max_speed
      self.mileage = mileage

modelX = Vehicle(240, 18)

print("model Max Speed:",modelX.max_speed)
print("model mileage:",modelX.mileage)
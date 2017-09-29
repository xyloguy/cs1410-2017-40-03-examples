from car import Car

c = Car()
print(c.setSpeed(-1))
print(c.setSpeed(80.1))
print(c.setSpeed(40.))
print(c.accelerate(85.0))
print(c.accelerate(1.0))
print(c.accelerate(0))
print(c.accelerate(-1.))
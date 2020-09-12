# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle_Classifications:
    def __init__(self, name):
        self.name = name

    def says_class(self):
        print("This is a ", self.name)

class Vehicle_Types(Vehicle_Classifications):
    def __init__(self, v_type):
        self.v_type = v_type

    def says_types(self):
        print("This" + Vehicle_Classifications + "it is a", self.v_type)

y = Vehicle_Types("Ground-Vehicle")
x = Vehicle_Classifications("Vehicle")
y.says_types()
        

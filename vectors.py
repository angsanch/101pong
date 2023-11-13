##
## EPITECH PROJECT, 2023
## vectors.py
## File description:
## manage vectors
##

class Vector:
    x:float
    y:float
    z:float
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Vectors can only be added from other vectors.")
        return (Vector(other.x + self.x, other.y + self.y, other.z + self.z))
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Vectors can only be substracted from other vectors.")
        return (Vector(other.x - self.x, other.y - self.y, other.z - self.z))

    def __mul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise NotImplementedError("Vectors can only be multiplied by numbers.")
        return (Vector(self.x * other, self.y * other, self.z * other))

    def __str__(self):
        return (f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})")
            

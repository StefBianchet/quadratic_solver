import math

class QuadraticEquation:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        delta = self.b**2 - 4 * self.a * self.c
        if delta < 0:
            return None  # No real solutions
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return (x,)
        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-self.b + sqrt_delta) / (2 * self.a)
            x2 = (-self.b - sqrt_delta) / (2 * self.a)
            return (x1, x2)

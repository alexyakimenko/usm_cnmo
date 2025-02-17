import math

from methods.bisection import bisection_method;
from methods.chord import chord_method;
from methods.newton import newton_method;

# main function
def function(x: float) -> float:
    return math.exp(-0.5 * x) - 0.2 * x**2 + 1.0

if __name__ == '__main__':
    a = 2.0
    b = 3.0
    x, iteration = bisection_method(a, b, function)
    print(f'Bisection method: x = {x}, iteration count = {iteration}')
    x, iteration = chord_method(a, b, function)
    print(f'Chord method: x = {x}, iteration count = {iteration}')
    x, iteration = newton_method(a, function, lambda x: -0.5 * math.exp(-0.5 * x) - 0.4 * x)
    print(f'Newton method: x = {x}, iteration count = {iteration}')
    

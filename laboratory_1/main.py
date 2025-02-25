import math

from methods.bisection import bisection_method
from methods.chord import chord_method
from methods.newton import newton_method
from methods.simple_iter import simple_iter_method

# main function
def function(x: float) -> float:
    return math.exp(-0.5 * x) - 0.2 * x**2 + 1.0

def derivative(f, x, delta_x=1e-6):
    return (f(x + delta_x) - f(x)) / delta_x

if __name__ == '__main__':
    a = 2.0
    b = 3.0
    x, iteration = bisection_method(a, b, function)
    print(f'Bisection method: x = {x}, iteration count = {iteration}')
    x, iteration = chord_method(a, b, function)
    print(f'Chord method: x = {x}, iteration count = {iteration}')
    x, iteration = newton_method(a, function, lambda x: derivative(function, x))
    print(f'Newton method: x = {x}, iteration count = {iteration}')
    x, iteration = simple_iter_method(a, function, derivative)
    print(f'Simple iteration method: x = {x}, iteration count = {iteration}')
    

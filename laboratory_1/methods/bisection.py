import math

from typing import Tuple
from typing import Callable

from .constants import EPSILON

# bisection method that returns x where f(x) = 0 and iteration count
def bisection_method(a: float, b: float, function: Callable) -> Tuple[float, float]:
    if function(a) * function(b) > 0:
        raise ValueError('Function has the same sign at the ends of the interval')
    iteration = 0
    while True:
        iteration += 1
        x = (a + b) / 2
        if abs(function(x)) < EPSILON:
            return x, iteration
        if function(a) * function(x) < 0:
            b = x
        else:
            a = x

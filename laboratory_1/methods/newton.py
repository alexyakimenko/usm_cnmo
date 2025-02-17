from typing import Tuple
from typing import Callable

from .constants import EPSILON

# newton method that returns x where f(x) = 0 and iteration count
def newton_method(x: float, function: Callable, derivative: Callable) -> Tuple[float, float]:
    iteration = 0
    while True:
        iteration += 1
        x = x - function(x) / derivative(x)
        if abs(function(x)) < EPSILON:
            return x, iteration

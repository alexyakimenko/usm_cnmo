from typing import Tuple
from enum import Enum

EPSILON = 10e-4

class Method(Enum):
    Gauss = 0
    Jacob = 1
    
def system_solve(method: Method) -> Tuple[Tuple[float, ...], int]:
    x1 = x2 = x3 = x4 = 0
    iterations = 0

    while True:
        old_x1, old_x2, old_x3, old_x4 = x1, x2, x3, x4

        if method == Method.Jacob:
            x1 = 0.605 / 2.923 - 0.220 * old_x2 / 2.923 - 0.159 * old_x3 / 2.923 - 0.328 * old_x4 / 2.923
            x2 = 0.496 / 4.123 - 0.363 * old_x1 / 4.123 - 0.268 * old_x3 / 4.123 - 0.327 * old_x4 / 4.123
            x3 = 0.590 / 3.906 - 0.169 * old_x1 / 3.906 - 0.271 * old_x2 / 3.906 - 0.295 * old_x4 / 3.906
            x4 = 0.896 / 3.862 - 0.241 * old_x1 / 3.862 - 0.319 * old_x2 / 3.862 - 0.257 * old_x3 / 3.862
        if method == Method.Gauss:
            x1 = 0.605 / 2.923 - 0.220 * x2 / 2.923 - 0.159 * x3 / 2.923 - 0.328 * x4 / 2.923
            x2 = 0.496 / 4.123 - 0.363 * x1 / 4.123 - 0.268 * x3 / 4.123 - 0.327 * x4 / 4.123
            x3 = 0.590 / 3.906 - 0.169 * x1 / 3.906 - 0.271 * x2 / 3.906 - 0.295 * x4 / 3.906
            x4 = 0.896 / 3.862 - 0.241 * x1 / 3.862 - 0.319 * x2 / 3.862 - 0.257 * x3 / 3.862

        iterations += 1
        if(max(abs(x1 - old_x1), abs(x2 - old_x2), abs(x3 - old_x3), abs(x4 - old_x4)) < EPSILON):
            return ((x1, x2, x3, x4), iterations)
        

(result1, iterations1) = system_solve(method=Method.Jacob)
print(result1, iterations1)
(result2, iterations2) = system_solve(method=Method.Gauss)
print(result2, iterations2)
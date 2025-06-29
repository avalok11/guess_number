from math import sqrt
from typing import Optional


def add_numbers(x_variable: float, y_variable: float) -> float:
    return x_variable + y_variable


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return 'none'

    root = calculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}')


x_variable = 10
y_variable = 5

print('Сумма чисел:', add_numbers(x_variable, y_variable))

print(calc(25.5))

import math


def area(r):
    """
    Вычисляет площадь круга по радиусу

    r (int): радиус круга
    return (float): площадь круга

    Пример вызова:
        >>> area(3)
        28.274333882308138
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по радиусу

    r (int): радиус круга
    return (float): длина окружности

    Пример вызова:
        >>> perimeter(3)
        18.84955592153876
    """
    return 2 * math.pi * r

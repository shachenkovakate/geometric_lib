import math


def area(r):
    '''
    Возвращает площадь круга

        Параметры:
            r (float): радиус круга

        Возвращаемое значение:
            area (float): площадь круга
    '''
    
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            perimeter (float): длина окружности
    '''
    
    return 2 * math.pi * r


# Geometry Shapes Library

A simple Python library for calculating **areas** and **perimeters** of basic geometric shapes:  
- Circle  
- Rectangle  
- Square  
- Triangle  

Each shape is implemented in its own module, with straightforward functions for computations.

---

## Project Structure
- circle.py # Area and perimeter of a circle
- rectangle.py # Area and perimeter of a rectangle
- square.py # Area and perimeter of a square
- triangle.py # Area and perimeter of a triangle

## Usage
### 1. Circle
```python
import circle

print(circle.area(5))       # 78.53981633974483
    Возвращает площадь круга
 
         Параметры:
            r (float): радиус круга

        Возвращаемое значение:
            area (float): площадь круга

print(circle.perimeter(5))  # 31.41592653589793
    Возвращает длину окружности

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            perimeter (float): длина окружности
```

### 2. Rectangle
```python
import rectangle

print(rectangle.area(4, 6))      # 24
    Возвращает площадь прямоугольника

        Параметры:
            a (float): сторона прямоугольника
            b (float): смежная с ней сторона прямоугольника

        Возвращаемое значение:
            area (float): площадь прямоугольника

print(rectangle.perimeter(4, 6)) # 20
    Возвращает периметр прямоугольника

        Параметры:
            a (float): сторона прямоугольника
            b (float): смежная с ней сторона прямоугольника

        Возвращаемое значение:
            perimeter (float): периметр прямоугольника
```

### 3. Square
```python
import square

print(square.area(5))       # 25
    Возвращает площадь квадрата

        Параметры:
            a (float): сторона квадрата

        Возвращаемое значение:
            area (float): площадь квадрата

print(square.perimeter(5))  # 20
    Возвращает периметр квадрата

        Параметры:
            a (float): сторона квадрата

        Возвращаемое значение:
            perimeter (float): периметр квадрата
```

### 4. Triangle
```python
import triangle

print(triangle.area(6, 4))        # 12.0
    Возвращает площадь треугольника

        Параметры:
            a (float): основание треугольника
            h (float): высота треугольника, проведённая к этому основанию

        Возвращаемое значение:
            area (float): площадь треугольника

print(triangle.perimeter(3, 4, 5)) # 12
    Возвращает периметр треугольника

        Параметры:
            a (float): первая сторона треугольника
            b (float): вторая сторона треугольника
            c (float): третья сторона треугольника

        Возвращаемое значение:
            perimeter (float): периметр треугольника
```

## Commit history
```
972e3d7 (HEAD -> new_features_502020) made a new file to use triangles and fixed the "rectangle.py"
1d7791d made a new file to use rectangles
d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
8ba9aeb L-03: Circle and square added
```

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
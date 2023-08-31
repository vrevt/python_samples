import math

print(math.pi)

cost = -2.99
print(cost, math.trunc(cost), int(cost))

cost = -3.6
print(cost, math.floor(cost))

cost = -1.1
print(cost, math.ceil(cost))

pow(2, 5)
math.sqrt(1212)


radius = 30
# площадь круга с радиусом 30
area = math.pi * math.pow(radius, 2)
print(area)


# натуральный логарифм числа 10
number = math.log(10, math.e)
print(number)

print(f'{math.pi=}')

print(f'{math.log(10)}')

print(f'{math.exp(10)}')


# Синус, тангенс, косинус
print(math.sin(2 * math.pi / 180))
# 0.034899496702500969


# Квадратный корень
print(math.sqrt(144), math.sqrt(2))
# 12.0 1.4142135623730951

# Абсолютное значение, сумма
print(abs(-42.0), sum((1, 2, 3, 4)))
# 42.0 10




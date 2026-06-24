n = int(input('Кол-во чисел: '))
n1 = map(int, input('Через пробел числа: ').split())


numbers = set(n1)

print(len(numbers))

numbers = list(map(int, input().split()))
n = set()

for number in numbers:
    if number in n:
        print('YES')
    else:
        print('NO')
        n.add(number)

a = int(input())
b = int(input())


A = set()
B = set()


for _ in range(a):
    A.add(int(input()))

for _ in range(b):
    B.add(int(input()))


print(len(A.intersection(B)))
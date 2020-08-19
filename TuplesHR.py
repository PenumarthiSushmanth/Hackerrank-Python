l = []
n = int(input())
x = input().split()
for i in x:
    l.append(int(i))
tup = tuple(l)
print(hash(tup))

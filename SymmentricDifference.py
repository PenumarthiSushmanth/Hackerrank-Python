n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
lst=sorted(a.symmetric_difference(b))
for i in lst:
    print(i)
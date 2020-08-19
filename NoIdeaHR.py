m,n = map(int, input().split())
arr = list(map(int,input().split()))
s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))
happi=0
for i in arr:
    if i in s1:
        happi+=1
    if i in s2:
        happi-=1
print(happi)

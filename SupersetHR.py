a = set(map(int, input().split()))
c=0
for i in range(int(input())):
    x = set(map(int, input().split()))
    if not a.issuperset(x):
        c = c+1
        break
if c>0:
    print("False")
else:
    print("True")

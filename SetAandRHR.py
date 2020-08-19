#n = int(input())
#s=[]
#for i in range(n):
#    s.append(input())
#print(len(set(s)))
n=int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    l = input().split()
    if l[0]=="pop":
        s.pop()
    elif l[0]=="remove":
        s.remove(int(l[1]))
    elif l[0]=="discard":
        s.discard(int(l[1]))
print(sum(s))
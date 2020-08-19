n = int(input())
s1 = set(map(int, input().split()))
n1 = int(input())
for i in range(n1):
    task = input().split()
    ele = set(map(int, input().split()))
    if task[0]=="intersection_update":
        s1.intersection_update(ele)
    elif task[0]=="update":
        s1.update(ele)
    elif task[0]=="symmetric_difference_update":
        s1.symmetric_difference_update(ele)
    elif task[0]=="difference_update":
        s1.difference_update(ele)
print(sum(s1))
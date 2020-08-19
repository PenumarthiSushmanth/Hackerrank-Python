n = int(input())
score =[]
name =[]
for i in range(n):
    name.append(input())
    score.append(float(input()))
dis =dict()
for i in range(n):
    dis[name[i]] = score[i]
lst=[]
for k,v in dis.items():
    lst.append([v,k])
lst.sort()
l2 = lst.copy()
temp = lst[0]
for i in lst:
    if i[0]==temp[0]:
        l2.remove(i)

temp2 = l2[0]
for i in l2:
    if i[0]==temp2[0]:
        print(i[1])

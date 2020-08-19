n = int(input())
a = []
score=[]
line = input()
score = line.split()
for i in score:
    a.append(int(i))
a.sort()
score=a.copy()
temp = max(a)
for i in a:
    if i==temp:
        score.remove(i)
print(max(score))
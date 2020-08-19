lst=[]
n = int(input())

for i in range(n):
    task = input().split()
    if task[0] == "insert":
        lst.insert(int(task[1]), int(task[2]))
    elif task[0] == "remove":
        lst.remove(int(task[1]))
    elif task[0] == "append":
        lst.append(int(task[1]))
    elif task[0] == "sort":
        lst.sort()
    elif task[0] == "pop":
        lst.pop()
    elif task[0] == "reverse":
        lst.reverse()
    elif task[0] == "print":
        print(lst)


import array as arr
a = arr.array('i',[1,2,3,8,4,2])
#s = array('u',["sush", "naveen", "pati"])
f = arr.array('d', [1.1,2.5,3.8])
a.append(5)
a.pop()
print(a.index(1))
for i in range(len(a)):
    print(a[i])

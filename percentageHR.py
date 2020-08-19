n = int(input())
name = []
mat = []
phy = []
che = []
for i in range(0,n):
    st = input()
    st = st.split()
    name.append(st[0])
    mat.append(float(st[1]))
    phy.append(float(st[2]))
    che.append(float(st[3]))
count =0

x = input()
for j in name:
    if x == j:
       avg = (mat[count]+phy[count]+che[count])/3
    count = count+1

print(format(avg, '.1f'))


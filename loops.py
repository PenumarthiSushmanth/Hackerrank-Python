#x = input()
#x=int(x)
#i=0
#while i<x:
#    print(i**2)
#    i=i+1

#x= int(input())
#i=1
#st =''
#while i<=x:
#    st = st + str(i)
#    i=i+1
#print(st)

large = -1
small = None

while True:
    num = input()
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    if num > large:
        large = num
    if small == None:
        small = num
    elif num < small:
        small = num

print('Maximum is', large)
print('Minimum is', small)



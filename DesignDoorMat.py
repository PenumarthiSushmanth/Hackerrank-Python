n, w = map(int,input().split())
for i in range(1,n,2):
    print((i * ".|.").center(w, "-"))
print("WELCOME".center(w,"-"))
for i in range(n-2,-1,-2):
    print((i * ".|.").center(w, "-"))
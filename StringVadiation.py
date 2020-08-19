s = input()
c=0

for i in range(0, len(s)):
    if s[i].isalnum():
        c=c+1
if c>0:
    print("True")
    c=0
else:
    print("False")

for i in range(0, len(s)):
    if s[i].isalpha():
        c=c+1
if c>0:
    print("True")
    c=0
else:
    print("False")

for i in range(0, len(s)):
    if s[i].isdigit():
        c=c+1
if c>0:
    print("True")
    c=0
else:
    print("False")

for i in range(0, len(s)):
    if s[i].islower():
        c=c+1
if c>0:
    print("True")
    c=0
else:
    print("False")

for i in range(0, len(s)):
    if s[i].isupper():
        c=c+1
if c>0:
    print("True")
    c=0
else:
    print("False")
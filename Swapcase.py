s = input()
s1 = ""
lst =[]
for i in range(0, len(s)):
    if s[i].isupper():
        lst.append(s[i].lower())
    else:
        lst.append(s[i].upper())
for j in lst:
    s1 = s1+j
#s1 = "".join(lst)
print(s1)


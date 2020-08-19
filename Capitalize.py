#line = input()
#words = line.split()
#l = ""
#for word in words:
#s    word=word.capitalize()
#    l = l+" "+word
#print(l)

s =input()
for x in s.split():
    s = s.replace(x, x.capitalize())
print(s)

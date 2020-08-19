line = input()
width = int(input())
i=0
s = ""
while i < len(line):
    s = s + line[i:i+width] + "\n"
    i=i+width
print(s)
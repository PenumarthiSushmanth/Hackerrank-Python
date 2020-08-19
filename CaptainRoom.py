n = int(input())
count=dict()
l = list(map(int, input().split()))
for word in l:
    count[word]=count.get(word,0)+1
for k,v in count.items():
    if v!=n:
        print(k)
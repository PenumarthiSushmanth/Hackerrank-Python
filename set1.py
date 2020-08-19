def average(array):
    avg = sum(set(array))/len(set(array))
    return avg


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
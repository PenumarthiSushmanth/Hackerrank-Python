def count_substring(string, sub_string):
    a = len(string)
    b = len(sub_string)
    time = a - b + 1
    c = 0
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        for i in range(0, time):
            if sub_string != string[i:i+b]:
                continue
            else:
                c = c + 1
        return c



string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
def leapyear(num):
    if num%400==0:
        return 'True'
    elif num%100==0:
        return 'False'
    elif num%4==0:
        return 'True'
    else:
        return 'False'


x = input()
num = int(x)
print(leapyear(num))
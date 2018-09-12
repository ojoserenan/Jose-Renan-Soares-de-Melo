def func(n):
    bina = ''
    while n !=0 :
        bina = bina + str(n%2)
        n = int(n/2)
    return bina[::-1]
def func2(n):
    if n ==0:
        return ''
    else:
        return func2(n//2) + str(n%2)
n = int(input(''))
print(func2(n))
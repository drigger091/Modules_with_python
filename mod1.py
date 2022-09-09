def add(a,b):
    return a + b

def sub(a ,b):
    return a -b

def mul(a,b):
    return a * b

def divide(a,b):
    return a/b

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)

def pal(x):
    x1 = x[::-1]
    if x1 == x:
        return "Palindrome"
    else:
        return "not palindrome"

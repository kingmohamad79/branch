def fact(n):
    if n<= 1:
        return 1
    
    b = n + fact(n-1)

    return b


print(fact(3))
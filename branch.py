def fact(n:int):
    if n<= 1:
        return 1
    
    b = n + fact(n-1)

    return b

x = fact(5)
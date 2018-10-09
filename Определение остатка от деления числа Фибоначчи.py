def fib_mod(n,m):
    Fib1 = 0
    Fib2 = 1
    Fib_res = 0
    Fib_div = [0,1]
    k=0
    for i in range(2,6*m):
        Fib_div.append((Fib_div[-1]+Fib_div[-2])%m)
        k+=1
        if Fib_div[-1]==1 and Fib_div[-2]==0:
            break
    return Fib_div[(n%k)]
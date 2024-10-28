def fact(N):
    if N==0:
        return([1])
    elif N==1:
        return([1,1])
    else:
        f = fact(N-1)
        f.append(N * f[-1])
        return(f)
    
print(fact(10))
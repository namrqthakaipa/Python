import random as r

while True:
    n= r.randint(0,10)
    print("Generated number is ", n)
    
    try:
        reci =1/n
        print("Reciprocal is ", reci)
        
    except ZeroDivisionError:
        print("cannot be divided by zero")
        break
import random as r

while True:
    number = r.randint(0,10)
    print("Number generated is ",number)
    
    if number == 0:
        print("Zero encountered, Cannot divide the number by zero")
        break
    reci = 1/number
    print("Reciprocal :",reci)
    
    
    

    
"""Generate random integers less than 50
and printing it, unitil you get a
number divisible by 10 """

import random as r
a = 0
while True:
    a = r.randint(0, 50)
    
    if a % 10 == 0:
        print(a,": is divisible by 10")
        break
    print(a)

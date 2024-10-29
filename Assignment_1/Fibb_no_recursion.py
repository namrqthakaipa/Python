
""" Input a number and find the Fibonacci 
    numbers without the recursion 
"""
import time

count = int(input("Enter the number"))
ts = time.time()   #in seconds
print("Start time",ts)

sum = 0
n1=0
n2=1
print(n1)
print(n2)

while (count > 0):
    #time.sleep(1)
    n = n1+n2
    print(n)
    n1= n2
    n2 = n
    count = count - 1
    
ts2 = time.time()  #in seconds
print("End Time",ts2)
diff=ts2-ts
print("Difference in the",diff )
    
   
    

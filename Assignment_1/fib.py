
import time
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("enter the number"))


ts = time.time()
print("Start time",ts)

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
ts2 = time.time()
print("End time",ts2)
diff=ts2-ts
print("The time difference is ",diff)
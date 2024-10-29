# Get user input
import time

count = int(input("Enter the number: "))


ts = time.time()
print(ts)

def fib(n):
    time.sleep(1)
    if n == 1:
        return [0]
        #print(0)
    elif n == 2:
        return [0, 1]  
    else:
        series = fib(n - 1) 

        series.append(series[-1] + series[-2])  
        return series
    

result = fib(count)
print( result)

ts2 = time.time()
print(ts2)
diff=ts2-ts
print("Difference in the",diff )


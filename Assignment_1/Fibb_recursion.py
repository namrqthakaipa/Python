# Get user input
count = int(input("Enter the number: "))

def fib(n):
  
    if n == 1:
        return [0]  
    elif n == 2:
        return [0, 1]  
    else:
        series = fib(n - 1) 

        series.append(series[-1] + series[-2])  
        return series

result = fib(count)
print( result)

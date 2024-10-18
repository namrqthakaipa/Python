""" Input a number and find the Fibonacci 
    numbers without the recursion 
"""

count = int(input("Enter the number"))
sum = 0
n1=0
n2=1
print(n1)
print(n2)
while (count >0):
    n = n1+n2
    print(n)
    n1= n2
    n2 = n
    count = count - 1
    
   
    

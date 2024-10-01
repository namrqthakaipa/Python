"""Conditions and Loops"""

#Python iterator
print("iteration in python")
fruits= ("apple","banana", "orange")
fruits_it = iter(fruits)

print(next(fruits_it))
print(next(fruits_it))
print(next(fruits_it))

#Break and continue statements
print("\n")
print("This is a break and continue statements example")
for i in range(7):
    if(i%3 == 0):
        continue
    print("In the Continue loop" ,i)
    
for i in range(7):
    if(i%4 == 3):
        break
    print("In the Break loop" ,i)
print("Outside the break")

##functions
print("\n")
print("This is a function example")
def square(x):
    x_square = x* x
    return(x_square)
a =3
print("The square of the number a is",square(a))


def add(a,b):
    sum= a+b
    return(sum)
z=2
y=3
c=add(z,y)
print("Addition:",c)


## Default Arguments
print("/n")
print("This is a default argument example")
def my_square(x, print_flag=False):
    x_square = x * x
    if print_flag:
        print(x_square)
    return(x_square)

m = 5
n = my_square(m)
print("",n)
n = my_square(m, True)
print("",n)

##KeywordArguments
print("/n")
print("This is a keywordArguments example") 
def my_func1(name,age):
    print(f"Hello, {name} You are {age} years old")
    
my_func1(name="Namratha", age="25")
 
 
#Scope of the variabe
print("/n")
print("This is an example for scope of the variable")
a,b,c =10,20,30   
def my_func(a):
    global c
    a,b,c =1,2,3
    print(f"Inside the function: a ={a}, b={b}, c={c}")
        
my_func(a)
print(f"Outside the function: a ={a}, b={b}, c={c}")
        
#Variable-length arguments
print("\n")
print("This is variable-length arguments example")
def sum_all(*args):
    print("3rd Argumentis",args[2])
    print("2nd argument is",args[1])
    print("1st arguments",args[0])
    return sum(args)

a = sum_all(1,2,3)
print("sum of the variable-length arguments",a)


## Using key word arguments
print("\n")
print("This is a key word arguments example")
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} :{value}")
print_info(name="babita", age="25", city="bangalore")


##Recursion
print("\n")
print("This is a Recursion example")
def factorial(n):
    if n==1:
        return(1)
    else:
        return(n*factorial(n-1))
a=6
print("Factorial is:",factorial(a))

##Lambda function
print("\n")
print("This is the Lambda function")
square = lambda x :x*x
a= square(27)
print("The square of the function is ", a)


#Higher order functions
print("\n")
print("This is the Higher order function example")
def square(x):
    print("finding the square")
    return(x*x)
def cube(x):
    print("finding the cube")
    return(x*x*x)

def apply_func(f,value):
    return f(value)
a=5
if a%2 ==0:
    print("It is a even nummber")
    val = apply_func(square,a)
else:
    print("It is a odd nummber")
    val = apply_func(cube, a)
print(val)
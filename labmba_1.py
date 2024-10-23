''''Write a Python program to create a lambda function that adds
15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and prints the result.'''

num_x=int(input("enter a number X : "))
num_y=int(input("Enter a number Y : "))
fun1 = lambda x: x + 15
print("The number added with 15 is ", fun1(num_x))
fun2 = lambda x,y: x * y
print("The multiplication of aruguments x and y are ",fun2(num_x,num_y))


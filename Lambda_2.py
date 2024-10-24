'''Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
Sample Output:'''

func= lambda x,y: x ** y

a = int(input("Enter the number"))
b = int(input("Enter the power"))
print("the lambda function outputs", func(a,b))


'''Write a Python program to sort a list of tuples using Lambda.
Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

tup1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

func1 = sorted(tup1, key=lambda x: x[1])

print(func1)



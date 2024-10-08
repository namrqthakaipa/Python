import json

list1 = [1, 2, 3, 4]

tuple1 = ("a", "b", "c" ,"d")

dictionary1 = {"First_name" : "Namratha", "Last_name" : "kaipa", "occupation" : "Software developer"}

x = '{ "name":"Kaipa", "age":30, "city":"Bangalore"}'

#loads is used to convert the json to dictionary
json1 = json.loads(x)

print("This is the list",list1)

print("Printing the list values:")
for i in list1:
    print(i)
print("\n")    
 
print("This is the tuple",tuple1)

print("Printing the tuple values:")
for j in tuple1:
    print(j)
print("\n")    
 
print("Printing the dictionary values")
for i in dictionary1:
    print(i,":", dictionary1[i])
print("\n")

print("The json is converted into dictionary",json1)

for i in json1:
    print("Printing the json values ")
    print(i, ":", json1[i])

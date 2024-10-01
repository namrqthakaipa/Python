###List###
a = [1,2,4,65,95]
b = [9,8]
a.append(b)
print("After appending A to B",a)
a.extend(b)
print("After extending A yo B",a)
maximum= [1,9,-10,9]
print("Finding the Max of the list",max(maximum))
print("Finding the Min of the list",min(maximum))

###Tuples###
"""Tuples are immutable"""
z = (1,2,3,4,5,6,7)
print(z.index(1))


###Sets###
""" No repetation is repeated"""
"""set1 ={1,2,3,4 }
set1.add(0)
print(set1)
#a.remove(0)
print(set1)
a.discard(0)
print(set1)"""

##Dictionary##

d = {"name": "namratha", "last_name": "kaipa", "gender" :"Female"}
print("This is the type of dictionary:",type(d))
print("The items in the dictionary is:",d.items())
print("The length of the items is: ",len(d.items()))
print("The itemsin the dictionary is: ",d.items())

for k, v in d.items():
    print(k, ":", v)
    
# Creating a new pair

d["city"] ='bangalore'
print("Adding the new pair",d)

del d['city']
print(d)






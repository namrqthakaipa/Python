class Person:
    pass

an_employee = Person()
print(type(an_employee))


class Person1:
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name}."
p1 = Person1("Alice", 25)
p2 =Person1("bob",32)

print(p1.greet())
print(p2.greet())

print(p1.species)
print(p2.species)


#private and public classes
print("")
print("This is a public and private classes")
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age       # Accessing a private attribute
    def set_age(self, age):
        self.__age = age        # Modifying a private attribute
        
        pa = Person2("alice",25)
        print(pa.get_age())
        
        
#inheritance
print("")
print("Example for inheritance")
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # calls the parent class constructor
        self.breed = breed 
    def speak(self):
        return f"{self.name} barks."
            
man = Animal("John")
print(man.speak())
#dog =Dog("Hunter")
#print(dog.speak())
do1 =Dog("Hunter", "Golden retriever")



print("This is from the super function",do1.speak())



#polymorphism

class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "<eow!"
animals = [Dog(), Cat()]

for animals in animals:
    print(animals.speak())
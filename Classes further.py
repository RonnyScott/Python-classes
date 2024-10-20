class Person:
    
    def __init__(self, name, age, occupation):
        
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce_yourself(self):
       
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I work as a {self.occupation}.")

# Create objects of the Person class
person1 = Person("Ronny", 23, "Software Engineer")
person2 = Person("Bob", 35, "Teacher")


print(person1.name)    
print(person2.age)      
person1.introduce_yourself()  
person2.introduce_yourself()  
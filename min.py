class Dog:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def info(self):
        print(f"I am a dog.My name is {self.name}.I am {self.age} years old")
    
    def make_sound(self):
        print("Bark")
    
    
class Cat:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def info(self):
        print(f"I am a cat.My name is {self.name}.I am {self.age} years old")
    
    def make_sound(self):
        print("Meow")
        
cat1=Cat("Feng", 1)
cat1.info()
cat1.make_sound()

dog1=Dog("Shayshay", 3)
dog1.info()
dog1.make_sound()

            
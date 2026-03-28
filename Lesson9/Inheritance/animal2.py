class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound.")

    def description(self):
        print(f"This is an animal named {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


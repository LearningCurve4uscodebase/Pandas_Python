class Animal:
    def speak(self):
        print("Generic animal sound")
    def another_method(self):
        print("This is an another method for inheritance")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

animal = Animal()
animal.speak()
dog.another_method()
cat.another_method()
class mammal():
    def __init__(self):
        print("MAMMAL")
    
    def speak(self):
        print("HOWL")

class human(mammal):
    def __init__(self):
        mammal.__init__(self) # force inheritance
        print("HUMAN")
    
    def speak(self): # overloaded method
        print("HI")

class dog(mammal):
    def __init__(self):
        mammal.__init__(self) # force inheritance
        print("DOG")
    
    def speak(self):
        print("WOOF")

things = [mammal(), human(), dog(), human(), dog(), mammal()]
for item in things:
    item.speak()
    print("---")
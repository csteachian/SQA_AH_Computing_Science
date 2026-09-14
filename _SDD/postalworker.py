class Human():
    def __init__(self):
        self.age = 0
        self.gender = ''
        self.height = 0.0
        self.phoneNo = '01224 000000'

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

class PostalWorker(Human):
    def __init__(self):
        Human.__init__(self) # connects the two classes
        self.hasBlackCat = True
        self.postbag = [Letter() for x in range(10)]

    def getCat(self):
        return self.hasBlackCat

    def setAge(self, age): # polymorphic - overrides superclass
        self.age = age // 2

class Letter():
    def __init__(self):
        self.address = ''
        self.postcode = 'AB15 4PB'

    def getPostcode(self):
        return self.postcode

# main program
supreme = Human()
meera = PostalWorker()
supreme.setAge(42)
meera.setAge(36)
print(supreme.getAge())
print(meera.getAge())
# error no 1 coming up, deliberate HONEST
meera.postbag.append(Letter())
#supreme.postbag.append(Letter())
# error no 2 - arrays, also deliberate HONEST
people = [Human() for x in range(5)]
people[0] = supreme
people[1] = meera
people[1].postbag.append(Letter()) # This should not be possible because
# the people array has been defined as type Human. This means that postbag
# is not accessible, so an error is generated.
#Creating a class
class People():
    #initialization of a class 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #method to create a behaviour of the object
    def showDetails(self):
        print(self.name,self.age,self.gender)

p1= People("john",18,"M")
p1.showDetails()


class people():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def showDetails(self):
        print(self.name,self.age,self.gender)
#creation of different class objects
p1= people("John",18,"M")
p2= people("Mary",25,"F")
p3= people("Kevin",22,"M")
p4= people("Olga",32,"F")
#using the method with each different object
p1.showDetails()
p2.showDetails()
p3.showDetails()
p4.showDetails()

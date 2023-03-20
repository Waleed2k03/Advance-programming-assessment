class Dog () :
     
     def __init__(self, name, age, color,):
        self.name = name
        self.age = age
        self.color = color
     def display(self):
        print("Dog characteristics")
        print("Name  : ",self.name)
        print("Age : ", self.age)
        print("Color :",self.color) 
 
Dog1 = Dog("bolt",3,"White")
Dog1.display()
Dog2 = Dog("goofy",5,"brown")
Dog2.display()


#i saved name in person and =grade in derived cls and i only used one object for derived cls  and gave argumetn to the parent cls

class Person():
    def __init__(self,name):
        self.name=name
class student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        
        print(self.name,self.grade)

saai=student("saai krahaanth","O Grade")
saai.display()
        
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class maneger(employee):

    def __init__(self,name,salary,departmant):
        super().__init__(name,salary)
        self.departmant=departmant
    def display(self):
        
        print(self.name,self.salary,self.departmant)

s1=maneger("saai","232342354","cse")
s1.display()

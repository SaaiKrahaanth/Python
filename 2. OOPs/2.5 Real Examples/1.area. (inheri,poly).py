class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self,a,b):
        return(a*b)
a=rectangle()
print(a.area(10,20))
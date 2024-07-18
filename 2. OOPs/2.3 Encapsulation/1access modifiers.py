class company:
    def __init__(self):
        self.public_name="Google" #accessed and modify by any objects in and out the cls
        self._protected="Gooooogle" #viewed  by the obj of cls
        self.__privatename="Gooooogle"#viewed only inside the class method

    def method(self):
        print(self.__privatename)
    

ob=company()
print(ob.public_name)
ob.public_name="google"
print("i changed",ob.public_name)#public

print(ob._protected)#protected

ob.method()#private




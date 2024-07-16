class dad():
    def phn(self):
        print("dad phn")
class son(dad,mom):
    def lap(self):
        print("son lap")
class mom():
    def sweet(self):
        print("sweet")
vishal=son()
vishal.lap()
vishal.phn()

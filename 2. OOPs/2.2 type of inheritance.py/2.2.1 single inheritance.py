#one class uses another class
#SINGLE INHERITANCE
class dad():
    def phn(self):
        print("dad phn")
class son(dad):
    def lap(self):
        print("son lap")
vishal=son()
vishal.lap()
vishal.phn()
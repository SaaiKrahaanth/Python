class grandpa():
    def phn(self):
        print ("grandpa phn")
class dad(grandpa):
    def money(self):
        print("dad phn")
class son(dad):
    def lap(self):
        print("son lap")

vishal=son()
vishal.lap()
vishal.money()

sudha=dad()
sudha.phn()

vishal.phn()
class dad():
    def money(self):
        print("dad money acess")
class land():
    def lands(self):
        print ("land accesed")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
vishal=son1()
vishal.money()
vishal.lands()
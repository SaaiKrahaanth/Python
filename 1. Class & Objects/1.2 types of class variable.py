class phn:
    rate="1000000"#class variable DEFAULT TO ALL OBJ
    def __init__(self,brand,rate):
        self.brand=brand
        self.rate=rate #instance varible_CHANGES UPPON OBJ
    def display(self):
        print("BRAND:",self.brand)
        print("RATE:",self.rate)
phn.rate="1000"#class variable DEFAULT TO ALL OBJ

samsung=phn("samsung","50000")
samsung.display()
redmi=phn("redmi","40000")
redmi.display()
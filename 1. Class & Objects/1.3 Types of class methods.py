class lap():
    chrgeType="c"

    def __init__(self) -> None:
        self.var="s"
    @classmethod   #decorator for class method 
    def changeChrgeType(cls):
        cls.chrgeType="b"
        print(cls.chrgeType)
    @staticmethod #decorator for static method
    def info():
        print("static method")
    def get_data(self,vari):
        self.var=vari
        print(self.var) 
hp=lap()
hp.changeChrgeType()
hp.info()
hp.get_data("chrgre")

    
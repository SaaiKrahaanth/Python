
class a():
    def __init__(self):
        print ("a")
class b(a):
    def __init__(self):
        super().__init__()
        print ("b")
class c(b,a): #actully super gives priority to left side class inside ()
    def __init__(self):
        super().__init__()
        print ("c")
obj=c()

# method overriding occurs when a subclass provides a particular implementation of a method declared by one of its parent classes.
class animal():
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        
        print("dog barks")
class bird (animal):
    def sound(self):
        
        print ("birds sing")

man=animal()
man.sound()

puppy=dog()
puppy.sound()

parrot=bird()
parrot.sound()


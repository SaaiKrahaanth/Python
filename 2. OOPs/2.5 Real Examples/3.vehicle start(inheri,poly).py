class vehicle():
    def start(self):
        print("vehicle starts")
class car(vehicle):
    def start(self):
        print("car started")

helicopter=vehicle()
helicopter.start()

rolls_royce=car()
rolls_royce.start()

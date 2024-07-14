class kodaikanal:
    falls=True
    room_no=0
    hotel_name=""
    def hill(self,x):
        print("enjoy hill"+x)
        return (x)
    def bar(self):
        print("lets party")
sk=kodaikanal()
bk=kodaikanal()
sk.falls=True
bk.falls=True
sk.room_no=100
bk.room_no=102
sk.hotel_name="raj"
bk.hotel_name="sivaji"
print(bk.hill(bk.hotel_name))
print(sk.bar())




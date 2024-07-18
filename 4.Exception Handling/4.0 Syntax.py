try:
    a=int(input())
    b=int(input())
    print (d)
except ValueError as e:
    print("value error")
except NameError as e:
    print("name error")
except TypeError as e:
    print("TypeError")
except Exception as e:
    print("some error happend")
finally :
    print("always executed")
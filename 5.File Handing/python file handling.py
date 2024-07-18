file=open("5.File Handing/fruits file/fruits.txt","r")

#READ
print (file.read(4))#no of char

print(file.readline())#first line only

print(file.readlines())#read line as list

#WRITE
sk=open("5.File Handing/fruits file/fruits.txt","w")
sk.write("iam prime legendary")#replace the complete file

#APPEND AT LAST OF FILE
sk=open("5.File Handing/fruits file/fruits.txt","a")
sk.write("(added by append)")


#WRITE LIST OF LINES
sk=open("5.File Handing/fruits file/fruits.txt","a")
lst=["saai","the","legend"]
sk.writelines(lst)

sk.close()




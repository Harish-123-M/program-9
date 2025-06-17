f = open("C:\\Users\\MICLAB\\Desktop\\demo.txt","r")
print("The filepointer is at byte :",f.tell())
f.seek(10);
print("After reading, the filepointer is at:",f.tell())

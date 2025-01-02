file=open('whale.txt','r')
print(file.read(5))
file.close()


file=open('whale.txt','a')
file.write("\n I am Raza and I am 15 year old")
file.close()
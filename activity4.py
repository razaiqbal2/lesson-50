file1=open('whale.txt','r')
file2=open('odd.txt','a')

can=file1.readlines()

for o in range(1,len(can)+1):
    if o%2!=0:
        file2.write(can [o-1])


file1.close()
file2.close()


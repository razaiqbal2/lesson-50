file1=open('whale.txt','r')
file2=open('lion.txt','a')

for line in file1:
    if not line.startswith('Lion'):
        file2.write(line)

file1.close()
file2.close()
# file = open('data.txt','r')
# data = file.read()
# print(data)
# file.close()

# file = open("data.txt",'w')
# data = "This is your second file of text."
# file.write(data)
# file.close()

# file = open("data.txt",'x')
# data = "This is your second file of text."
# file.write(data)
# file.close()

# file = open("data.txt",'a')
# data = "This is your python class."
# file.write(data)
# file.close()

file = open("mysticker.png",'rb')

data = file.read()
print(data)
file.close()

file = open("mysticker2.png",'wb')
file.write(data)
file.close()
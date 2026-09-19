file=open("server.txt", "r")      #open opens the file in read mode
content= file.read()
print(content)
file.close()  # this closes the file after reading it
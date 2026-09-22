with open("write.txt","w") as file:
    file.write("Hello Adinarayana\n")
    file.write("Hello Khiranya Srini\n")
    file.write("Hello Friya\n")
    file.write("Hello Srikanth\n")

with open("write.txt","a") as file:
    file.write("--------from Append Mode--------\n")
    file.write("Hello Nanna\n")
    file.write("Practice in Sept 22\n")
    file.write("TEST")
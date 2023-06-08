# ______________________________________________________________________________________________________________
# READ A FILE 

f= open("a_text_file.txt","r") # r mode is default if we write like this --> f=open("a_text_file") ,it will work as it is 
print(f)
text_in_file=f.read()
print(text_in_file)
# f.close()

# _______________________________________________________________________________________________________________
# WRITE A FILE 
w= open("a_text_file.txt", "w")
w.write("write hello world")
text_in_file=f.read() #here w cant be used to read the file as w is used for oopening file in write  mode
print(text_in_file)
w.close()

# ________________________________________________________________________________________________________________
# APPEND A FILE 
a=open("a_text_file.txt","a")
a.write(" append hello world ")
text_in_file=f.read()
print(text_in_file)
a.close()


with open('a_text_file.txt', "a") as ma:
    # as soon as we move out of this block(indentation) file will be closed automatically
    ma.write(" no need to close file in this syntax")
    
    print(f.read())

# readline function 
f = open("a_text_file.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)


# writelines() function
f= open("myTextFile2.txt", 'w') # automatically create a textfile name myTextFile2.txt if if doesnot exist
lines=['line 1 \n', "line 2 \n", "line 3 \n"]
f.writelines(lines)
f.close()

# seek(), tell() and truncate()
with open("myTextFile3.txt" , 'r') as f:
    print(type(f))

    #move to 10th in the byte 
    f.seek(10)

    print(f.tell()) # tell the cursor position in file 

    #read the next 5 bytes 
    data= f.read(5)
    print(data)

with open("myTextFile3.txt", "w") as f:
    f.truncate(5)

with open("myTextFile3.txt", 'r') as f:
    print(f.read())
    




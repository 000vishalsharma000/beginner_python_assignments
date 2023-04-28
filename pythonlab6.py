# Experiment-6
# I. Write a Python program to read an entire text file.
# II. Write a Python program to read a file line by line and store it into a list.
# III. Write a Python program to combine each line from first file with the corresponding line
# in second file.
# IV. Write a Python program that takes a text file as input and returns the number of words of
# a given text file.

# Note: Some words can be separated by a comma with no space.
# V. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to
# Z.txt.

# VI. Write a Python program to create a file where all letters of English alphabet are listed by
# specified number of letters on each line.

import os

#1
def read_file():
    with open("lab6_text_file.txt", "r") as tf:
        content=tf.read()
        print(content)

read_file()

#2
def file_to_list():
    file_lst=[]
    f= open("lab6_text_file.txt", "r")
    while True:
        line= f.readline()
        if not line:
            break
        file_lst.append(line)

    print(file_lst)   

file_to_list()

#3
def concat_file_by_line():
    f1=open("lab6_firstFile.txt", "r")
    f2=open("lab6_secondFile.txt", "r")
    w=open("concatenated_file.txt", "w")
    while True :
        line_f1=f1.readline()[0:-1]
        line_f2=f2.readline()[0:-1]

        if not (line_f1 or line_f2):
            break

        w.write(line_f1+line_f2+"\n")
    
    w=open("concatenated_file.txt", "r")
    print(w.read())
    

concat_file_by_line()

#4
def count_word_in_file():
    with open("lab6_text_file.txt", "r") as nw:
        full_file=nw.read()
        word_arr =full_file.split(" ")
        word_count=len(word_arr)
    
    print(word_count)

count_word_in_file()

#5
def make_abcd_text_files():
    if( not os.path.exists("lab6_abcd_text_files")):
        os.mkdir("lab6_abcd_text_files")

    for i in range(0,26+1):
        if( not os.path.exists(f"lab6_abcd_text_files/{chr(65 +i)}.txt")):
            os.mkdir(f"lab6_abcd_text_files/{chr(65 +i)}.txt")

#6
def alphabet_in_order():
    with open("alphabet_order.txt", 'w') as ao:
        for i in range(0,26):
            ao.write(f"{i+1}-{chr(i+65)}\n")
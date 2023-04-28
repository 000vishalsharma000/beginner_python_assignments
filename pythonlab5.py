#1
def string_to_list(any_string):
    lst=list(any_string)
    print(lst)

string_to_list("python")

#2
def first_repeated_word(sentence ):
    import re
    lst=re.split("\\s+", sentence)
    print(lst)

    for i in range(len(lst)):
        for j in range(i):
            if(lst[i] ==lst[j]):
                print("'",lst[i], "'" , ": first repeated word")
                return True

first_repeated_word('vishal       is is a good   bad good  ')

#3
def find_common_characters(string1, string2):
    str1=string1.lower()
    str2=string2.lower()

    list_of_common_char=set()

    for char in str1:
        if char in str2:
            list_of_common_char.add(char)

    lexicographical_order=sorted(list_of_common_char)
    print("common character in both strings are : ", lexicographical_order)

find_common_characters("vishaal", "SHARMA")
    
#4
def substrings_of_repeated_and_unique_chars(a_string):
    count_lst=list(map(lambda c:a_string.count(c), a_string))
    print(count_lst)

    unique_char_str=""
    repeated_char_str=""

    for i in range(len(count_lst)):
        if(a_string[i] != " "):
            if(count_lst[i]>1):
                repeated_char_str+=a_string[i]
            else:
                unique_char_str+=a_string[i]
    

    print("string of unique character : ",unique_char_str)
    print("string of repeated characters : ",repeated_char_str)

substrings_of_repeated_and_unique_chars("vishal sharma")
    
#5
def find_substr_index(string, substring):
    index=string.find(substring)
    if index>=0:
        print(f"'{substring}' is found in string={string} at index={index}")
    else:
        print(f"substring '{substring}' is not found in string {string}")

find_substr_index("vishal", "i")













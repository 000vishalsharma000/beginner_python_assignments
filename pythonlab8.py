
#1
tpl=(1,3,5,7,8,2,4)

def index_in_tuple(tpl,element):
    idx=tpl.index(element)
    print(f"index of {element} is {idx}")

index_in_tuple(tpl,3)

#2
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
 
def unzip_list_of_tuples(list_of_tpl):
    print("Original list is : " + str(list_of_tpl))

    res = list(zip(*list_of_tpl))
    print("Modified list is : " + str(res))

unzip_list_of_tuples(test_list)

#3
sample_data=[(),(),(),(","),("a","b"),("a","b","c"),("d")]

def remove_empty_tuples(list_of_tpl):
    empty_count=list_of_tpl.count(())

    for i in range(empty_count):
        list_of_tpl.remove(())

    print(list_of_tpl)

remove_empty_tuples(sample_data)

#4
key_dictionary={"a":1, "b":2, "c":3, "d":4}

def is_key_present(dictionary, passed_key):
    for key in dictionary:
        if key== passed_key:
            print(f"{passed_key} is present in dictionary : {dictionary}")
            return True
    
    print(f"{passed_key} is not present in dictionary : {dictionary}")
    return False 
    
    
        
is_key_present(key_dictionary,"c")

#5
def square_dictionary(num_range):
    num_square_dict={}
    for i in range (num_range+1):
        num_square_dict[i]=i**2
    
    print(num_square_dict)

square_dictionary(5)

#6
num_dict={"one":1, "two":2 , "three":3 , "four":4}

def min_max_values_in_dict(dictionary):
    all_dict_values= dictionary.values()
    print("allvalues of dictionary", all_dict_values)
    mx=max(all_dict_values)
    mn=min(all_dict_values)
    print(f"min value :{mn} max value :{mx}")

min_max_values_in_dict(num_dict)

#7
data =[{"id": 1, "success": True, "name": "vishal"}, {"id": 2, "success": False, "name": "sharma"}, {"id": 3, "success": True, "name": "guddu"}]

def count_key_value(list_of_dicts, key, val):
    count=0

    for dictionay in list_of_dicts:
        if dictionay[key]==val:
            count+=1
    
    print(f"total no of dictinaries in data that have {key}={val} are : {count}")

count_key_value(data, "success", True)

#8
class_list=['class5', 'class6', 'class7', 'class8']
num_list=[1,2,2,3]

def make_dict_from_two_list(li1,li2):
    list_dict={}
    for key, val in zip(li1, li2):
        list_dict[key]=val
    
    print(list_dict)

make_dict_from_two_list(class_list,num_list)
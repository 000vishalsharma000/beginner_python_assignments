#................................................ PYTHON LAB 7............................................

#1
def multiply_all_in_list(lst):
    from functools import reduce
    prod_all=reduce(lambda i, j: i*j, lst)
    print(prod_all)

multiply_all_in_list([1,2,3,4])

#2
def filter_strings(str_lst):
    filterlst= list(filter(lambda i: i[0]==i[-1] and len(i)>=2, str_lst))
    print(filterlst, " no of string= ", len(filterlst))

filter_strings(["gang", "a", "mum", "sprachen", "oo", "train"])

#3

def have_common_element(lst1,lst2):
    set1=set(lst1)
    set2=set(lst2)
    intersection= set1 & set2
    if len(intersection)>0:
        return True
    else:
        return False
    
print(have_common_element([1, 3,5,7,9],[2,4,5,6]))

#4
def firstLastFive_sq_vals():
    first_sq_vals=[i*i for i in range(1,6) ]
    last_sq_vals=[i*i for i in range(26,31) ]
    sq_vals=first_sq_vals+last_sq_vals
    print(sq_vals)

firstLastFive_sq_vals()

#5
def circularly_identical(lst1, lst2):
    st1=set(lst1)
    st2=set(lst2)
    if st1&st2==st1 and st1&st2==st2 :
        print("symmetrically identical ")
    else :
        print("not symmtrically equal ")

circularly_identical([1,2,3,4], [2,3,4,1])
    
#6
def sort_list_of_objects(list_of_pairs):
    sorted_list = sorted(list_of_pairs, key=lambda x: x[0]) # defining key to sort list of custom objects 
    print(sorted_list)                                      # its equivalent to comparator in java

sort_list_of_objects([(9,"i"), (2,"b"), (8, "h"), (3,"c"), (6,"f"), (5,"e")])

#7
def list_to_listOfDict(l1, l2):
    eng_letter_dict=[]
    for c,s in zip(l1, l2):
        eng_letter_dict.append({"capital letter": c, "small letter" : s})

    print(eng_letter_dict)

list_to_listOfDict(["A","B", "C", "D"], ["a","b","c","d"])

#8
def find_smallest_second_index(tuples_list):
    """
    Find the tuple with the smallest second index value from a list of tuples.
    """
    print("smallest tuple: " ,min(tuples_list, key=lambda x: x[1]))  # key can also be defined in min function using lambda function
                                                                     # where our lamda func is equivalent to comparator of java 
 
find_smallest_second_index([(1, 3), (2, 1), (3, 5), (4, 2)])

#9
def is_all_dict_empty(list_of_dict):
    for dictionary in list_of_dict:
        if len(dictionary) !=0:
            return False
    return True

print(is_all_dict_empty([{},{},{}]))
print(is_all_dict_empty([{1,2},{},{}]))





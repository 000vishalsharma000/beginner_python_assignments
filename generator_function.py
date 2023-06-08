# generator function in python ________________________________________________________________________________________

# 1. generator fuction do lazy evaluation means only generate only one value at a time when required

# 2. it uses [yeild] instead of (return)

# 3. it is a evaluation stratergy which delays evaluation of an expression untill its value is needed 

# 4. lib  func that implement this are 
        # i. range()
        # ii. zip()
        # iii. open()
        # iv. map()


def fib(n):
    first, second = 0, 1
    for i in range(n):
        print("generating values for i =", i)
        if i in (0, 1):
            yield i      #<-- use yield instead of return to make normal function to generator 
        else:
            first, second = second, first+second
            yield second


for i in fib(5):
    # now our defined function fib(n) is behaving smthing like range function of python
    print(i)

print("printing every element generated by generator function one by one using generator object and .next() function ")
gnratr_obj = fib(5)
next(gnratr_obj)    # generate one value at a time
next(gnratr_obj)   # gnerate nexxt value in fib(5) associated with generator object

print("generator khatam ")
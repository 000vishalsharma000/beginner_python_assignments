# a decorator function for hello which also greet the user
# decorator function are usulally used to modify our existing function
def greet(func):
    def mod_func():
        print("good morning \n")
        func()
        print("thanks for using this function ")

    return mod_func


@greet        # if we write @<decorator function name > before any function ,
              # when we call that fuction anywhere in our program 
              # the decorator functoion for that particular function will be called 
              # rather the actuall function
def hello():
    print("hello world")


hello()

# if we have not written [ @greet ] on top of our hello function
# we have to call our decorator function like below ( greet(hello)() )
# to get same out put , try commenting out @greet statement then greet(hello)() will give same output as
#  calling hello after defining a decorator function for hello(greet in our case )
greet(hello)()


# decorator function with argument
def add_decorator(fx):
    def mfx(*args, **kwargs): 
        #*args : to accept any no of positional aguments 
        # **kargs : to accept any no of key value pair in format "key=value"
        print("adding two nums ")
        fx(*args, **kwargs)
        print("addition decorator function completed ")

    return mfx


@add_decorator
def add(a, b):
    print(a+b)


add(3, 5)
add_decorator(add)(3, 5)


###############################################################################################################

# usage of ** kargs_________________________________
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Alice", age=30, city="New York")

# usage of * args___________________________________
def my_function(*args):
    for arg in args:
        print(arg)

my_function('apple', 'banana', 'cherry')

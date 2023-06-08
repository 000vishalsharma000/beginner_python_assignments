#  __doc__ in python (doc string)

class Dog:
    """ your best friend """  # this give info of what class does , should come immediately after class name declaration (no blank line )

    def do_nothing(self):
        """ does nothing really """
        pass


billo=Dog()
billo.do_nothing()
print(billo.__doc__) # this--> { __funcName__ } notation is called a (dunder_method / magic_method) in python 
print(Dog.__doc__)

# application of __doc__ : we can use SPHINX python documentation generator to generate documentation webpage for our moodule/software 
# when we have defined a docstring for a method while we are typing its name in a code editor whatever written in docString is displayed in method info snippet/popup

# #function: -A function is a block of code which only runs when it is called.You can pass data, known as parameters, into a function.A function can return data as a result.
def my_function():
    print("I am a function")
my_function()   #function calling 


def my_function1():
    a=int(input("enter the value: "))#taking value from the user 
    print(a)
my_function1()


def my_function2():
    a=int(input("enter the value: "))#taking value from the user 
    a=a+2
    print(a)
my_function2()

# there are two types of functons :-                                                                            1.parametarised function :- the parametarised function are those function which carries the parameter or the parameters defined within the function itself.eg:- my_ufunction(int a,intb)                                     2.Non-Parameterised functon :- the non-parameterised functions are those function which do not carres the parameters or there function is empty eg:- my_function() 


def function(a=int(input("enter the value of a: "))):#parameterised functions 
    if(a>10):
        a=a+2
        print("the value of a is: ",a)
function()

def function():#non-parameterised function
    a=10
    if(a>0):
        a=a%2
        print("the remainder is: ",a)
function()

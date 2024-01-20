# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

#NOTE:- the indentation error will leads to the error in the program.
a=int(input("Enter the value of a: "))
if a>=0:  #the if statement puts up the condition.
    a=a+2 #after the condition is satified the operation to be performed.
    print(a)

#elif:- the elif leads to the second condition during the execution of the code if the first if conditon is turned to be false

a=int (input("enter the value of a:"))
b= int (input("Enter the value of b: "))
if a>b:
    c=a+b
    print(c)
elif a==b:
    print("both are same")

#else :- the else again leads to the execution of the second condition same as the elif does if the first condition of if statement is false.

a=2
b=4
if a>b:
    print(a)
    print("a is grater than b!")
elif a==b:
    print("both the values are same")
else:
    print(b)
    print("b is grater than a!")

a=int (input("Enter the value of a: "))
b=int(input("Enter the value of b:"))
larger_number=max(a,b)
print("the larger number is:",larger_number)
if a>b:larger_number=a
else:larger_number=b

print(larger_number)

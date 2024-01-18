#type casting is the method to convert the python variable data-type into a certain data type in order to perform the required operation by the user.There are two types of type casting implicit and explicit type casting .                                                                                                        The imlicit type casting:- the implicit type casting the automatic conversion of one data type to other data type.
a=5
b="hey how are you"
c=6.0
print(type(a))
print(type(b))
print(type(c))

#explicit type conversion:- the variables data type are cinverted by the user to fullfil the required data type.
a=5
b=float(a) #conversion from integer data type to float data type.
print(a,type(a))
print(b, type(b))

a=5
b=str(a) #conversion of integer data type to string data type.
print(type(a))
print(b,type(b))

a="5"
b= float(a) #conversion of string data type to float data type.
print(a, type(a))
print(b, type(b))

a="5"
b= int(a) #conversion of string data type to int data type.
print(a, type(a))
print(b, type(b))


#further lets discuss about some strings in detail....

a="1"
b="1"
print(a+b)#in case of strings the + operand becomes the concatenation symbol means to add the two strings.
c=int(a)
d=int(b)
print(c+d)

a=5
b="2"  
print(a*b) #in case of multilictaion * denotes the occurance of the string for n number of integers 
print(b*a)
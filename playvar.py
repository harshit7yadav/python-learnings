#lets talk about some whats variables in the python program is about variable are the value storing characters or string which stores the value assigned to them such as var=3 therefore here the set of characters var is the variable which stores the value assigned to it 3.
var =3
print(var)
#the above mentioned is a basic explanation of variables but lets figure out if changing in the values to the same value does cause any changes or not.

var =3 
var=4 #here what we found is intially the value assigned to the variable var is 3 but on passing again value to the same variable leads to over-writing.Therefore the value 3 will be over-written by 4.
print(var)

#furthermore lets perform some operations on the variables including the types of variables 
mary=3
jerry=2
aein=4
add=mary+jerry+aein #addition  
sub=mary-jerry-aein #substraction 
multi=mary*jerry*aein #multiplictaion 
c=((mary*jerry)+aein)
div= mary/aein#division(gives the quiotient on dividing the two numbers (here variables) )
mod=aein%jerry #modulus (gives the remainder on dividing the two numbers (here variables) )
intdev=mary//aein #// id is the integer devision where the result lacks the fractional parts i.e gives integer output for the integer values and gives 0 output for the float values 
# print(add)
# print(sub)
# print(multi)
# print(c)
# print(div)
# print(mod)
# print(intdev)
print(add, sub, multi, c, div, mod, intdev)
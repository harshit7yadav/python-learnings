#Looping :- looping is the way to represent the iterative or repetative occurance of an element or event 
#we will be discussing some of the different lopping methods further below
# 1. While loop:- while(condition){
#                                   do}
x=2
while x!=0: #infinite loop 
     print("True for a reason")

x=int(input("Enter the value: "))
while x!=0:
     if x%2==0:
        print("the number is even")
     elif x%2!=0:
        print("the number is odd")
     else:
        print("the number is ZERO")

#FOR Loop :- for loop is another kind of loop which is used to count the number of loops to check the condition.
#for loop is used for definite number i.e counts the number of times the loop jhave been executed.
for i in range(10):
    print(i)

for i in range(2,8):
    print(i)  #counts the starting value mentioned in range but excludes the laste or maximum value 2>=i<8

for i in range(2,6,2): #the third value inserted in the range is the increment value by default is conted to be 1.
    print(i)

#THE BREAK AND CONTINUE STATEMENTS WITHIN THE LOOP :=
#BREAK :- the break statement within the looping statement take out from the loop weather the looping statement is may or may not be true 

for i in range(10,20):
    i=i+1
    print(i)
    break
print(i+2)


for i in range(20,30,3):
    print(i)
    continue
print(i+5)


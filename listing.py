# Lists are used to store multiple items in a single variable.# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.# Lists are created using square brackets.
numbers=[2, 3, 4]
print(numbers)
print(numbers[1])#list are kind of array which are used to store the certain data such a integers or string or aplhanumeriic numbers. list also allows indexing means using the index from 0 to n-1 elements can be extract using the indexing.here in print(numbers[1]),[1] denotes the first index value in the given list.

#inserting the new elements to the list 

numbers=[2, 3, 4]
print(numbers)
numbers.insert(3,10)#insert(also append()) new element to the list
print("the new list is:", numbers)

#delete an element from the list 

numbers=[2, 3, 4]
print(numbers)
del numbers[1]#delete or remove new element to the list
print("the new list is:", numbers)

#changing the list items :
numbers=[2, 3, 4]
numbers[1]=2#replace the element at the given index value
print(numbers)


#the same could be done with strings too:

str=["Jhanvi","yash","ankit"]
print(str)
print(str[1])
#print(str[3])#error
str.insert(3,"harshit")
print("the new string list obtained is :", str)
del str[0]
print("the new string list obtained is :", str)
str[0]="Jhanvi"
print("the new string list obtained is :", str)


#negative indices unn python programming count the indexes from the back excluding 0 
str=["Jhanvi","yash","ankit"]
print(str[-1])

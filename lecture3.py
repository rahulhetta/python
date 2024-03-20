# LISTS IN PYTHON
marks = [95,65,65,98,87,67,65]
print(marks)
print(type(marks))
# WE CAN ALSO FIND MARKS AT DIFFERENT INDEX
print(marks[2])
print(marks[5])
#STRINGS are imutable / LISTS are mutable

marks= [54,54,98,87,65,98,93,93]
print(marks[2:6])

#LIST METHODS
#APPEND METHOD- add element in the list/ list.append()
list = [3,4,5,6,7]
list.append(2)
print(list)

#SORT METHOD- sorts in accending order/ LIST.SORT()
list = [3,6,5,4,7,2,8,9]
print(list.sort())
print(list)

#SORT IN DECINDING ORDER /list.sort(reverse=true)
list = [2,3,4,5,6,7,8]
print(list.sort(reverse= True)) # T capital
print(list)
#SORTING also arange alphabets 

#REVERSE METHOD - opposite the list
list = [2,4,6,8,9,5]
list.reverse()
print(list)

#INSERT METHOD - insert element in index
list = [2,3,4,5]
list.insert(4,5)
print(list)

#REMOVE METHOD - remove first occurance of element 
list= [2,4,6,8,9]
list.remove(4)
print(list)

#POP METHOD - remove element from a particular index
list = [2,3,4,5,6,7]
list.pop(2)
print(list)

#TUPLES IN PYTHON - Built in datatype lets us create immutable seqeence of values
tup=(4,) # tuples always ends with comma(,)
print(tup)

#TUPLES METHODS

# tup.index(el) - returns index of first occurance
tup = (1,2,3,4,5)
print(tup.index(2))

#COUNT METHOD count total occurance 
tup=(1,2,2,2,3,4,5,6)
print(tup.count(2))


str1="this is string"
str2='this is string'
str3="""this is string"""

str1="this is string.\n and i am rahul"
print(str1)

# CONCATINATION - PROCESS OF ADDITION OF TWO STRINGS 
str1="rahul"
str2="hetta"
print(str1+str2)

#WE CAN ALSO DO THIS INSTEAD
str1="rahul"
str2="hetta"
final_str=str1+str2
print(final_str)

#LENGTH OF STR  len(str)
print(len(str1))
#WE CAN ALSO DO THIS INSTEAD
len1=len(str1)
print(len1)

#INDEXING - COUNTING OR GIVING A COUNT TO CHARACTERS IN STRING
# WE CAN ONLY ACCESS THE CHARACTER BUT CANT CHANGE OR REPLACE IT 
str="rahul hetta"
ch=str[9]
print(ch)

# SLICING- ACCESSING PARTS OF STRING
str="rahul hetta"
print(str[1:8])  #TO REACH THE LAST (str[5:])

#STRING FUNCTION
# (1) str.endswith("ta")  return true if string ends with ta
str1= "my name is rahul hetta"
print(str.endswith("ta"))

#(2) CAPITALIZE  capitalize the string
str1= "my name is rahul hetta"
print(str1.capitalize())
# (3) REPLACE FUNCTION replace old value with new one 
str="i am studing python from apna collage"
print(str.replace("o","a"))
#(4) FIND FUNCTION used to find a word in a string 
str= "my name is rahul hetta from shimla"
print(str.find("from"))

name =input ("enter your name")
print("length of your name is ",len(name))

# to find r in string
str="heya my name is rahul rahul ragul"
print(str.count("r"))

3 #CONDITION STATEMENT if-elif-else
age=21

if(age >= 18):
    print("can drive ans also vote ")

light="red"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")   #INDENTATION - proper spacing in python instead of {}
else:
    print("light is broken")  

# LETS TRY
marks = int(input("enter the mark of student:"))
if(marks >= 90):
    print("GRADE = A")
elif(marks >= 80):
    print("GRADE = B")
elif(marks >= 70):
    print("GRADE = C")
elif(marks > 70):
    print("GRADE = D") 
else:
    print("bosdk tu fail hogya hai ")  

#NESTING- ek statement ke andar dusri statement ko likhna             
age = 45
if (age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
     


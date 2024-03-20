#DICTONARIES IN PYTHON
info = {
   "key" : "value",
   "name" : "rahul",
   "sem"  : "fourth",
}
print(info)

student = {
    "name" : "rahul",
    "subjects" : {
        "chem" : 97,
        "physic" : 65,
        "maths" : 56
    }
}
print(student["subjects"]["maths"])
print(len(list(student.keys())))

#mydict.items() - returns the key according to value
print(student["name"]) # jab name2 likha instead of name it will show erroe
print(student.get("name")) # but it will show nonw 

#mydict.update(newdict) - inserts the specified item to the dictionary
student = {
    "name" : "rahul",
    "subjects" : {
        "phy" : 97,
        "chem" : 66,
        "maths" : 45,
    }
}
print(student["subject"]["maths"])
# to update or add city
student.update({"city" : "delhi"})
print(student)
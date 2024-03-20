#print nmber 1- 100
i = 1
while i <= 100:
    print(i)
    i += 1

#print number 100 - 1
i = 100
while i >= 1: #stoping condition
    print(i)
    i -= 1  

#print multiplication table of 3
i=1
while i <=10:
    print(3*i)
    i += 1   
# printing table of random no
n = int(input("enter number :"))    
i=1
while i <=10:
    print(n*i)
    i += 1       

# print the element of list using loop
    #[1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,24,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
# list of heros
heroes = ["ironman","batman","spiderman"] 

idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1 

# search a number in tbis list using loop
nums = [1,4,9,16,24,36,49,64,81,100]

x=100

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx",i)
    i += 1

# FOR LOOP- used for sequential traversal
    #for traversing list , tuples 
veges = ["alloo","gobhi","matar"]
for val in veges:
    print(val)


        


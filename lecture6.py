#FUNCTION - block of statement that perform a specific task
def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(10,5)

#lines of codes between

calc_sum(6,7)

# lets make a function to calculate average of threenumbers
def calc_avg(a,b,c,):
    sum = (a+b+c)
    avg = sum/3
    print(avg)
    return avg

calc_avg(1, 6, 7)
# RECURSION - when a function call itself repeately
#recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)


show(5) 

def fact(n):
    if(n == 1 or n==0 ):
        return 1
    return fact(n-1)*n   

print(fact(6))


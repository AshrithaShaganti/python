#count the number of digits
def count(n):
    c=0
    while(n>0):
        c+=1
        n=n//10
    return c

n=int(input("enter a number:"))
print("number of digits in",n,"is",count(n))
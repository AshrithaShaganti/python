#check whether a number is positive or negative
def check(num):
    if(num>0):
        print("number is positive")
    elif(num==0):
        print("number is equal to zero")
    else:
        print("number is negative")
x=int(input("enter a number:"))
check(x)
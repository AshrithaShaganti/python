#check whether the number is divisible by 5 and 11
def fun(x):
    if(x%5==0 and x%11==0):
        return True
    else:
        return False
a=int(input("enter a number:"))
v=fun(a)
if(v==True):
    print("divisible by both 5 and 11")
else:
    print("not divisible by both 5 and 11")
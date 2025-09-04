#factorail of a given number
def fact(n):
    f=1
    i=1
    if(n==0 or n==1):
        f=1
    else:
        while(i<=n):
            f=f*i
            i+=1
    return f
num=int(input('enter a number:'))
print("factorial of",num,"is",fact(num))
    
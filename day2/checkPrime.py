#to check whether a number is prime or not
def prime(n):
    count=0
    i=1
    while(i in range(n+1)):
        if(n%i==0):
            count+=1
        i=i+1
    if(count==2):
        return "prime number"
    else:
        return "not a prime number"
n=int(input("enter a number:"))
print(n,"is",prime(n))
def findfl(n):
    l=n%10
    while(n>0):
        r=n%10
        n=n//10
    print("first digit:",r)
    print("last digit:",l)

print(findfl(1234))
        

        

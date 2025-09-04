def palindromes(n):
    for i in range(1,n+1):
        rev=0
        temp=i
        while(i>0):
            r=i%10
            rev=rev*10+r
            i//=10
        if(temp==rev):
            print(temp)

palindromes(int(input("Enter n:")))
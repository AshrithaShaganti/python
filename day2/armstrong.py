def armstrong(n):
    for i in range(1,n+1):
        m=len(str(n))
        rev=0
        temp=i
        while(i>0):
            r=i%10
            rev=rev+r**m
            i//=10
        if(temp==rev):
            print(temp)
armstrong(int(input("Enter n:")))
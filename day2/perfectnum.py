def perfect(n):
    for i in range(1,n+1):
        sum=0
        temp=i
        for j in range(1,i):
            if(i%j==0):
                sum+=j
        if(sum==temp):
            print(temp)

perfect(int(input("enter n:")))


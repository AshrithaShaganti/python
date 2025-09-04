def primefactors(n):
    for j in range(n+1):
        if(n%j==0):
            count=0
            while(i<=j):

                if(j%i==0):
                    count+=1
            if(count==2):
                print(j)

primefactors(int(input("enter a number")))
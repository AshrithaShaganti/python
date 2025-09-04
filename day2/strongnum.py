
def strong(n):
    for i in range(1,n+1):
        sum=0
        r=i%10
        if(r==0 or r==1):
            fact=1
        else:
            while(j in range(2,r+1)):
                fact=fact*j
                j+=1
        sum+=fact
        n//=10

    
num=int(input('enter a number:'))
strong(num)
    
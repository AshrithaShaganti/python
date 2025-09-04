def notes(amount):
    a=[2000,500,200,100,50,20,10,5,2,1]
    #count=0
    n=0
    for i in a:
        if(amount>=i):
            count=amount//i
            amount=amount%i
            n+=1
    return n
print(notes(int(input("enter an amount:"))))
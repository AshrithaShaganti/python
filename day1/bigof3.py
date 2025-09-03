#greatest of 3 numbers
def big3(a,b,c):
    if(a>b):
        if(a>c):
            print(a,"is greatest")
        else:
            print(c,"is greatest")
    else:
        print(c,"is greatest")
x,y,z=map(int,input("enter 3 numbers:").split())
big3(x,y,z)
#even or odd
def evenodd(num):
    if(num%2==0):
        print(num,"is even number")
    else:
        print(num,"is an odd number")
x=int(input("enter a number:"))
evenodd(x)
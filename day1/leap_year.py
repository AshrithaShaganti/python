#leap year or not
def leap(x):
    if x%4==0:
        print(x,"is a Leap year")
    else:
        print(x,"is not a leap year")
a=int(input("enter year:"))
leap(a)
#current bill generation
def bill(u):
    if(u<=50):
        b=u*3.80
        return b
    elif(u>50 and u<=100):
        b=(50*3.80)+(u-50)*4.20
        return b
    elif(u>100 and u<=200):
        b=(50*3.80)+(50*4.20)+(u-100)*5.10
        return b
    elif(u>200 and u<=300):
        b=(50*3.80)+(50*4.20)+(100)*5.10+(u-200)*6.30
        return b
    elif(u>300):
        b=(50*3.80)+(50*4.20)+(100)*5.10+(100)*6.30+(u-300)*7.50
        return b
    else:
        return ""
x=int(input("enter the number of units:"))
b=bill(x)
print("Your bill is:",b)
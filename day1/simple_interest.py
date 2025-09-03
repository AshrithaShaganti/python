p=int(input("enter principle amount:"))
t=int(input("enter no.of months:"))
r=int(input("enter interest rate:"))
si=(p*t*r)/100
total=si+p
print("interest amount:",si)
print("total amount:",total)
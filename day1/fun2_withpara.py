#function with arguments and no return type  
'''def add(a,b):
    c=a+b
    print("sum=",c)
x=input("enter x value:")
y=input("enter y value:")
add(x,y)'''

'''def kmTomiles(miles):
    miles=int(km)*0.621371
    print("distance in miles=",miles)

km=input("enter distance in kilometers:")
kmTomiles(km)'''

#convert days to years and months
def convert(days):
    year=days/365
    months=int(days/30)
    print(days,'days equals',months,'months,',year,'years')
x=int(input("enter number of days:"))
convert(x)
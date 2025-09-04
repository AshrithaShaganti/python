def week(x):
    if(x==0):
        return "sunday"
    elif(x==1):
        return "monday"
    elif(x==2):
        return "tuesday"
    elif(x==3):
        return "wednesday"
    elif(x==4):
        return "thursday"
    elif(x==5):
        return "friday"
    elif(x==6):
        return "saturday"
    else:
        return "invalid data"
a=int(input("enter a number between 0 t0 6:"))
day=week(a)
print(day)
      
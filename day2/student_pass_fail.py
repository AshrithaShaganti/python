'''
print('total marks=',total)
print("Average of 3=",round(avg,2))'''

def sgrade(name,rno,x,y,z):
    total=x+y+z
    a=(total)/3
    print("Student details")
    print('-------------------------')
    print('Name:',name)
    print('Roll number:',rno)
    if(x>=40 and y>=40 and z>=40):
        if(a>=80):
            return "Distinction"
        elif(a>=71 and a<80):
            return "A"
        elif(a>=51 and a<=70):
            return "B"
        else:
            return "C"
    else:
        return "FAIL"
name=input("enter name of the student:")
rno=input("enter the roll number:")
math=int(input("enter marks in maths:"))
phy=int(input("enter marks in physics:"))
chem=int(input("enter marks in chemistry:"))
g=sgrade(name,rno,math,phy,chem)
print("Grade is:",g)
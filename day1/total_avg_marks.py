name=input("enter name of the student:")
rno=input("enter the roll number:")
math=int(input("enter marks in maths:"))
phy=int(input("enter marks in physics:"))
chem=int(input("enter marks in chemistry:"))
total=math+phy+chem
avg=(total)/3

print("Student details")
print('-------------------------')
print('Name:',name)
print('Roll number:',rno)
print('total marks=',total)
print("Average of 3=",round(avg,2))
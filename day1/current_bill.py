
#current bill calculation
name=input("enter the consumer name:")
num=input("enter the consumer number:")
pmr=input("enter present month reading:")
lmr=input("enter last month reading:")
units=float(pmr)-float(lmr)
bill=units*3.80
print('\n')
print("         Consumer Details             ")
print('------------------------------------------')
print('Name:',name)
print('Consumer number:',num)
print('Current Bill=',round(bill,2))

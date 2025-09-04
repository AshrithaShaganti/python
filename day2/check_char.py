#check what the given char is
def check(ch):
    if ('a'<=ch<='z'):
        return "lowercase alphabet"
    elif('A'<=ch<='Z'):
        return "uppercase alphabet"
    elif(ch>="0" and ch<"9"):
        return "number"
    else:
        return "special character"
x=input("enter a character:")
a=check(x)
print(x,"is a",a)
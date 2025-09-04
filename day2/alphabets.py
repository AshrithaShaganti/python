#to print alphabets from a to z using while loop
def alphabets():
    i=97 #ascii value for 'a' is 97
    while(i<=122):
        print(chr(i))
        i+=1
alphabets()
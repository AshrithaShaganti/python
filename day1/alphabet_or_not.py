#check whether a character is an alphabet or not
def alphabet(ch):
    if('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        print(ch,"is alphabet")
    else:
        print(ch,"is not an alphabet")
alphabet('A')
def num_to_words(n):
    words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    if n == 0:
        print("zero")
        return

    rev = 0
    temp = n
    while temp > 0:
        r = temp % 10
        rev = rev * 10 + r
        temp //= 10

    while rev > 0:
        r = rev % 10
        print(words[r], end=" ")
        rev //= 10

        
n=int(input("enter a number:"))
num_to_words(n)

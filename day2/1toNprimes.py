# Print prime numbers between 1 and n
def primes(n):
    for i in range(2, n+1):   
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:   
            print(i)

primes(int(input("Enter n: ")))

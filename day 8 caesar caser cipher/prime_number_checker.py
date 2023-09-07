numberr = int(input("enter the prime number"))

def prime_number(number):
    is_prime = False
    for i in range(2 , number):
        number % i == 0
        is_prime = True

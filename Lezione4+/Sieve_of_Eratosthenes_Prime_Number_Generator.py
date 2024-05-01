# Gioele Amendola
# 01/05/2024

# Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
# Initialize an array of all numbers up to the limit, marking each number as prime initially.
# Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
# The remaining unmarked numbers are the prime numbers within the limit. Return the list of prime numbers.

def prime_list(limit: int = None):
    
    # Input limit if None
    if limit is None:
        while True:
            try:
                limit = int(input("Input limit for the prime numbers: "))
                if limit < 1:
                    raise ValueError
            except:
                print("Number non valid")
            else:
                break
    # Check limit if argument
    elif limit < 1:
        raise ValueError("limit number is less than one.")
    elif type(limit) != int:
        raise ValueError("limit number is not an integer.")


    # Creation of dictionary of all numbers up to the limit
    check_prime: dict = {i:True for i in range(1,limit+1)}

    # Find prime numbers with Eratosthenes algorithm
    for number in range(2,limit+1):
        if check_prime[number] == True and number != limit-1:
            for index in range(number+1,limit+1):
                check_prime[index] = False if index%number == 0 or check_prime[index] == False else True
    
    # Creation of a list with all the prime numbers found with the algorithm
    primes: list = [number for number in range(1,limit+1) if check_prime[number] == True]

    return primes

# Test Example:
print(prime_list())
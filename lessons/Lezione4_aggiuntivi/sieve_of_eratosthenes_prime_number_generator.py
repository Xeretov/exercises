'''
Module providing a function that calculates a list of
prime numbers following the sieve of erastosthenes algorithm.
    

# Gioele Amendola
# 01/05/2024

# Create a function that generates a list of prime numbers
# up to a specified limit using the Sieve of Eratosthenes algorithm.
# Initialize an array of all numbers up to the limit, marking each number as prime initially.
# Iterate through the array, starting from 2,
# and mark every multiple of the current number as non-prime.
# The remaining unmarked numbers are the prime numbers within the limit.
# Return the list of prime numbers.
'''
def prime_list(limit: int = None) -> list:
    '''
    It calculates a list of prime numbers and returns it.

    Args:
        limit (int, optional): The maximum range of the list. Defaults to None.

    Raises:
        ValueError: If limit is not a number greater than 1.

    Returns:
        list: list of prime numbers
    '''
    # Input limit if None
    if limit is None:
        while True:
            try:
                limit = int(input("Input limit for the prime numbers: "))
                if limit < 1:
                    raise ValueError
            except ValueError:
                print("Number not valid")
            else:
                break
    # Check limit if argument
    elif limit < 1:
        raise ValueError("limit number is less than one.")
    elif not isinstance(limit,int):
        raise ValueError("limit number is not an integer.")


    # Creation of dictionary of all numbers up to the limit
    check_prime: dict = {i:True for i in range(1,limit+1)}

    # Find prime numbers with Eratosthenes algorithm
    for number in range(2,limit+1):
        if check_prime[number] is True and number != limit-1:
            i: int = 2
            while number*i <= limit:
                check_prime[number*i] = False
                i += 1
        if not True in list(check_prime.values())[number:]:
            break

    # Creation of a list with all the prime numbers found with the algorithm
    primes: list = [number for number in range(1,limit+1) if check_prime[number] is True]

    return primes

# Test Example:
print(prime_list())
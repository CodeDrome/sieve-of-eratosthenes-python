from typing import List


PRIME_COL = "\x1B[32m"
COMPOSITE_COL = "\x1B[31m"
RESET_COL = "\x1B[0m"


def main():

    """
    The main function creates and runs the sieve, using the various other functions below.
    """

    print("-------------------------")
    print("| codedrome.com         |")
    print("| Sieve of Eratosthenes |")
    print("-------------------------\n")

    # Create a list of specified size, initially all set to True
    max = 200
    sieve = [True] * (max + 1)
    p = 2

    print("Initial state: all marked as prime")
    print_sieve(sieve, 10)

    print("Running Sieve of Eratosthenes...")

    while(p != -1):

        mark_multiples(sieve, max, p)
        p = find_next_prime(sieve, max, p)

    print("Composite numbers now identified")
    print(PRIME_COL + "Prime numbers" + RESET_COL)
    print(COMPOSITE_COL + "Composite numbers" + RESET_COL)
    print_sieve(sieve, 10)


def print_sieve(sieve: List, columncount: int):

    """
    Prints the sieve in columns of specified size.
    Primes and composites are printed in the colours
    specified at the top of the file, using ANSI terminal codes.
    """

    for i in range(1, len(sieve)):

        if sieve[i] == True:

            print(f"{PRIME_COL}{i:4d}{RESET_COL}", end="")

        else:

            print(f"{COMPOSITE_COL}{i:4d}{RESET_COL}", end="")

        if i % columncount == 0:
            print("")


def mark_multiples(sieve: List, max: int, p: int):

    """
    Given a prime, mark all its multiples as False (ie non-prime or composite)
    up to the given maximum.
    """

    multiplier = 2
    i = p * multiplier

    if i <= max:

        while(i <= max):

            sieve[i] = False
            multiplier+=1
            i = p * multiplier


def find_next_prime(sieve: List, max: int, current: int):

    """
    Iterates remaining part of sieve to find next prime.
    Returns it if found, or -1 if it gets to the end
    without finding any more primes.
    """

    for i in range(current + 1, max + 1):

        if sieve[i] == True:

            return i

    return -1


if __name__ == "__main__":

    main()

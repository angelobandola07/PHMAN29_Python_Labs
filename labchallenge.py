def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check potential factors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_and_save_primes(limit=250, filename="prime_numbers.txt"):
    # Generate the list of prime numbers
    primes = [num for num in range(1, limit + 1) if is_prime(num)]
    
    # Display the results in the console
    print(f"Prime numbers between 1 and {limit}:")
    print(primes)
    print(f"\nTotal prime numbers found: {len(primes)}")
    
    # Write the results to a text file
    with open(filename, "w") as file:
        file.write(f"Prime numbers between 1 and {limit}:\n")
        file.write("-" * 35 + "\n")
        for prime in primes:
            file.write(f"{prime}\n")
            
    print(f"\nResults successfully saved to '{filename}'.")

if __name__ == "__main__":
    generate_and_save_primes(250)
def generate_fibonacci(n: int) -> list:
    """
    Generates the Fibonacci sequence up to n terms.
    Parameters:
        n (int): Number of terms to generate.
    Returns:
        list: Fibonacci sequence as a list of integers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    return fib

def main():
    print("Fibonacci Sequence Generator")
    
    while True:
        try:
            num = int(input("Enter the number of terms (positive integer): "))
            if num < 0:
                print("Please enter a non-negative integer.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.\n")
    
    sequence = generate_fibonacci(num)
    print(f"\nFibonacci sequence with {num} term(s):")
    print(sequence)

if __name__ == "__main__":
    main()

# Function to calculate the Fibonacci number for a given position n
def Fibonacci(n):
    # Check if the input is invalid (negative number)
    if n < 0:
        print("Incorrect input")  # Print error message for invalid input
        return None  # Exit the function
    
    # Base case: If n is 0, return 0 as the Fibonacci number
    elif n == 0:
        return 0
    
    # Base case: If n is 1 or 2, return 1 as the Fibonacci number
    elif n == 1 or n == 2:
        return 1
    
    # Recursive case: Calculate Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# Driver code
try:
    # Prompt the user to enter the number of terms they want in the Fibonacci series
    num = int(input("Enter the number of terms for the Fibonacci series: "))
    
    # Check if the input number is a positive integer
    if num <= 0:
        print("Please enter a positive integer.")  # Error message for non-positive input
    else:
        print("Fibonacci series:")  # Print header for the output
        # Loop to print Fibonacci numbers from 0 to (num-1)
        for i in range(num):
            print(Fibonacci(i), end=" ")  # Print each Fibonacci number separated by a space
except ValueError:
    # Handle the case where the input is not an integer
    print("Please enter a valid integer.")

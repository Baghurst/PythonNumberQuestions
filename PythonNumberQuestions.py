#1
n = int(input("Enter a number: "))
value = 1
while value <= n:
    if value % 5 == 0:
        value += 1
        continue
    print(value)
    value += 1

#2
    
   # Ask the user for a value of n
n = int(input("Enter a value for n: "))

# Initialize the starting number
current = 1

# Initialize an iteration counter
iterations = 0

# Start the while loop to print numbers up to n squared
while current <= n ** 2:
    print(current)
    
    # Increment the current number and iteration count
    current += 1
    iterations += 1
    
    # Check if the iteration count has reached 50
    if iterations == 50:
        print("Reached 50 iterations, stopping early.")
        break  # Stop the loop if 50 iterations are reached

#3

# Loop through numbers from 3 to 29
for num in range(3, 30):
    # Check if the number is odd and not a multiple of 5
    if num % 2 != 0 and num % 5 != 0:
        print(num)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
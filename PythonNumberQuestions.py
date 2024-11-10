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
    
n = int(input("Enter a value for n: "))
current = 1
iterations = 0
while current <= n ** 2:
    print(current)
    current += 1
    iterations += 1
    if iterations == 50:
        print("Reached 50 iterations, stopping early.")
        break

#3 

for num in range(3, 30):
    if num % 2 != 0 and num % 5 != 0:
        print(num)
    
#4    

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
multiple_to_ignore = int(input("Enter the multiple to ignore: "))
for num in range(start, end + 1):
    if num % 2 != 0 and num % multiple_to_ignore != 0:
        print(num)
    
#5    

for num in range(50, 19, -1):
    if num % 2 == 0 and num % 3 != 0:
        print(num)
    
#6    

for num in range(12, -15, -2):
    print(num)

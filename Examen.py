number = 1 # Initialize the variable
while number < 8: # Complete the while loop condition
    print(number, end=" ")
    number += 1 # Increment the variable

# Should print 1 2 3 4 5 6 7 


for number in range(2, 13, 2):
    print(number)

# Should print:
# 2
# 4
# 6
# 8
# 10
# 12


def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n: # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1 # Increment the appropriate variable
        current_number += 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1
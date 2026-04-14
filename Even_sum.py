# Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Calculate sum of even numbers
even_sum = 0
for num in arr:
    if num % 2 == 0:
        even_sum += num

# Print result
print(even_sum)

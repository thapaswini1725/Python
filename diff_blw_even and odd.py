# Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

even_sum = 0
odd_sum = 0

# Calculate sums
for num in arr:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Absolute difference
result = abs(even_sum - odd_sum)

# Print result
print(result)

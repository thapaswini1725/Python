#Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Calculate sum of odd numbers
odd_sum = 0
for num in arr:
    if num % 2 != 0:
        odd_sum += num

# Print result
print(odd_sum)

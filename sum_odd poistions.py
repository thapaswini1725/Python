# Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Calculate sum of odd index elements
odd_index_sum = 0
for i in range(n):
    if i % 2 != 0:
        odd_index_sum += arr[i]

# Print result
print(odd_index_sum)

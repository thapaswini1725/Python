# Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Find last odd index
last_index = -1

for i in range(n):
    if arr[i] % 2 != 0:
        last_index = i

# Print result
print(last_index)

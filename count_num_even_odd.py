# Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

count = 0

# Check from index 1 to n-2
for i in range(1, n-1):
    if arr[i] % 2 != 0 and arr[i-1] % 2 == 0 and arr[i+1] % 2 == 0:
        count += 1

# Print result
print(count)

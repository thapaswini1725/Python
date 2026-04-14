# Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Calculate integer average
avg = sum(arr) // n

# Check if average is present
if avg in arr:
    print(True)
else:
    print(False)

# Read size of array
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Element to search
key = int(input())

# Check presence
if key in arr:
    print(True)
else:
    print(False)

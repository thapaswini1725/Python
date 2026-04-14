# Read size
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Calculate average (floor division)
avg = sum(arr) // n

# Count elements >= average
count = 0
for num in arr:
    if num >= avg:
        count += 1

print(count)

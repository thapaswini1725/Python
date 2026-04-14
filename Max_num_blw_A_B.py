 Read size
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

# Read A and B
A, B = map(int, input().split())

# Filter elements between A and B (inclusive)
filtered = [x for x in arr if A <= x <= B]

# Print result
if filtered:
    print(max(filtered))
else:
    print(-1)

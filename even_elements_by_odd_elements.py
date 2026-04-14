# `Read size
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

even = []
odd = []

# Separate elements
for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

# Combine and print
result = even + odd
print(*result)

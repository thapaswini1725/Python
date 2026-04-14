# Read size
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

odd = []
even = []

# Separate elements
for num in arr:
    if num % 2 != 0:
        odd.append(num)
    else:
        even.append(num)

# Combine and print
result = odd + even
print(*result)

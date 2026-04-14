# Read size
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

count = 0

for i in range(n):
    prev = arr[(i - 1) % n]
    next_ = arr[(i + 1) % n]
    
    if prev % 2 != next_ % 2:
        count += 1

print(count)

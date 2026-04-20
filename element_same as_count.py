# Read size
n = int(input())

# Read array
arr = list(map(int, input().split()))

# Count frequency
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

result = []
seen = set()

# Maintain order and avoid duplicates
for num in arr:
    if num == freq[num] and num not in seen:
        result.append(num)
        seen.add(num)

# Output
if result:
    print(*result)
else:
    print(-1)

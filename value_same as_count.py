n = int(input())
arr = list(map(int, input().split()))

count = [0] * 10   # since elements are from 1 to 9

# Count frequency
for num in arr:
    count[num] += 1

result = 0

# Check condition
for i in range(1, 10):
    if count[i] == i:
        result += 1

print(result)

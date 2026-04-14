# Read size
n = int(input())

# Read array elements
arr = list(map(int, input().split()))

decimal = 0

for i in range(n):
    decimal = decimal * 2 + arr[i]

print(decimal)

#Read size
n = int(input())

# Read array
arr = list(map(int, input().split()))

is_even_array = True

for num in arr:
    if num % 2 != 0:
        is_even_array = False
        break

print(is_even_array)

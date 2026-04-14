n = int(input())

sum_factors = 0

for i in range(1, n // 2 + 1):
    if n % i == 0:
        sum_factors += i

if sum_factors > n:
    print("True")
else:
    print("False")

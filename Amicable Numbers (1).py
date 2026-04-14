n = int(input())
m = int(input())

def sum_of_proper_divisors(x):
    s = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            s += i
    return s

if n != m and sum_of_proper_divisors(n) == m and sum_of_proper_divisors(m) == n:
    print("Amicable")
else:
    print("Not Amicable")
n = int(input())

sum_factors = 0

for i in range(1, n // 2 + 1):
    if n % i == 0:
        sum_factors += i

if sum_factors > n:
    print("True")
else:
    print("False")

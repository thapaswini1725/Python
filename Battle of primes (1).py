n1 = int(input())
n2 = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

total = n1 + n2

for k in range(1, 10001):
    if is_prime(total + k):
        print(k)
        break

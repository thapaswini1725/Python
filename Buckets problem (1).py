# Read inputs
N = int(input())
T = int(input())

# State of buckets
# 0 -> all empty
# 1 -> all filled
# 2 -> only odd buckets filled
# 3 -> only even buckets filled
state = 0

for _ in range(T):
    task = int(input())

    if task == 1:
        state = 1
    elif task == 2:
        if state == 1:
            state = 2
        elif state == 3:
            state = 0
    elif task == 3:
        if state == 1:
            state = 3
        elif state == 2:
            state = 0
    elif task == 4:
        state = 0

# Calculate result
if state == 1:
    print(N)
elif state == 2:
    print((N + 1) // 2)   # odd buckets
elif state == 3:
    print(N // 2)         # even buckets
else:
    print(0)

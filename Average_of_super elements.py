# Read size
n = int(input())

# Read array
arr = list(map(int, input().split()))

# Count frequency
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

# Find super elements (unique values)
super_elements = []

for num in freq:
    if num == freq[num]:
        super_elements.append(num)

# Output
if super_elements:
    avg = sum(super_elements) / len(super_elements)
    print(f"{avg:.2f}")
else:
    print(-1)

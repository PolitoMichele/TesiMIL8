import random

n = 20
c = 0
objects = []

for _ in range(n):
    s = random.randint(1, 100)
    w = s+10
    c += s
    objects.append((w, s))

c = c // 10

with open("input.txt", "w") as f:
    f.write(f"{n} {c}\n")
    for w, s in objects:
        f.write(f"{w} {s}\n")
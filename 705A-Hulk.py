n = int(input())
i = 1
l = []
while i <= n:
    if i % 2 == 0:
        l.append("that I love")
    else:
        l.append("that I hate")
    i = i + 1
l.append("it")
l = " ".join(l)
l = l.split()
print(" ".join(l[1:]))

m = input()
n = input()
i = 0
l = []
while i < len(m):
    t = int(m[i]) - int(n[i])
    if t < 0:
        t = t * -1
        l.append(str(t))
    else:
        l.append(str(t))
    i = i + 1
print("".join(l))

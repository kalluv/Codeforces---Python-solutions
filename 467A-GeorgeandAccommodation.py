n = int(input())
i = 0
l = []
while i < n:
    m = input()
    p,q = m.split()
    p,q = int(p), int(q)
    if p < q and (q - p) >= 2:
        l.append(p)
    i = i + 1
print(len(l))

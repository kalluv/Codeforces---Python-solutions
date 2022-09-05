s = input()
n, h = s.split()
m = input()
m = m.split()
l = []
i = 0
while i < len(m):
    if int(m[i]) < int(h):
        m[i] = 1
        l.append(m[i])
    elif int(m[i]) == int(h):
        m[i] = 1
        l.append(m[i])
    else:
        m[i] = 2
        l.append(m[i])
    i = i + 1
i = 0
t = 0
while i < len(l):
    t = t + l[i]
    i = i + 1
print(t)

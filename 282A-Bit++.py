n = int(input())
i = 0
t = []
while i < n:
    m = input()
    t.append(m)
    i = i + 1
i = 0
s = []
while i < len(t):
    if t[i] == "++X":
        s.append(1)
    elif t[i] == "X++":
        s.append(1)
    elif t[i] == "--X":
        s.append(-1)
    else:
        s.append(-1)
    i = i + 1
i = 0
t = 0
while i < len(s):
    t = t + s[i]
    i = i + 1
print(t)

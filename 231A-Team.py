n = int(input())
i = 0
t = 0
while i < n:
    s = input()
    s = s.split()
    if s.count("1") > 1:
        s = 1
    else:
        s = 0
    t = t + s
    i = i + 1
print(t)

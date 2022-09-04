n = int(input())
i = 0
l = []
t = 0
while i < n:
    m = input()
    left, enter = m.split()
    left = int(left)
    enter = int(enter)
    t = t - left + enter
    l.append(t)
    i = i + 1
print(max(l))

m = int(input())
s = input()
s = s.split()
l = []
for x in s:
    l.append(int(x))
print("{:.12f}".format(sum(l)/m))

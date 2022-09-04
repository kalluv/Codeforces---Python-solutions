s = input()
l = []
s = list(s)
for x in s:
    if x not in l:
        l.append(x)
if len(l) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

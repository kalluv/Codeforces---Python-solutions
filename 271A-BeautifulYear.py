n = int(input())
def unique_num(s):
    l = []
    for x in str(s):
        if x not in l:
            l.append(x)
    if len(l) == len(str(s)):
        n = int(("").join(l))
        return n
    return "non unique number"
i = 0
l = []
while i < 10000:
    if i >= 1000 and i > n and str(unique_num(i)).isdigit() == True:
        l.append(i)
    i = i + 1
print(min(l))

n = int(input())
i = 0
while i < n:
    s = input()
    if len(s) > 10:
        s = list(s)
        a, b, c = s[0], s[-1], s[1:-1]
        c = "".join(c)
        print(a + str(len(c)) + b)
    else:
        print(s)
    i = i + 1

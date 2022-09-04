s = input()
if s[0].islower() == True:
    l = s[0].upper()
    s = s[1:]
    print(l + s)
else:
    print(s)

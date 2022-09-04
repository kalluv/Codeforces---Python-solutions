s = input()
 
s = s.split()
 
n = int(s[-1])
 
i = 1
t = 0
while i <= n:
    price = i * int(s[0])
    t = t + price
    i = i + 1
 
if (t - int(s[1])) > 0:
    print(t - int(s[1]))
else:
    print(0)

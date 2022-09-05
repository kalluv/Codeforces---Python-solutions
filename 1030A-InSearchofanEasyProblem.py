m = input()
n = input()
l = []
for x in n.split():
    if x == "1":
        l.append("HARD")
    elif x == "0":
        l.append("EASY")
if l.count("HARD") >= 1:
    print("HARD")
elif l.count("EASY") == len(l):
    print("EASY")

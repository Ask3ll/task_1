a = input().split(" ")
a = list(map(int, a))
b = input().split(" ")
c = input().split(" ")
d = input().split(" ")
d = list(map(int, d))
points = 0
for i in b:
    if i in c:
        points+=d[c.index(i)+1]
    else:
        points+=d[0]
print(points)
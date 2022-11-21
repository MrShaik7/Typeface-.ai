s1,s2 = input().split(",")
s1 = s1[1:-1]
s2 = s2[1:-1]
s = s2[-1]
c = 0
for i in s1:
    if i==s:
        c += 1
print(c)
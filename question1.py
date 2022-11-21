n = int(input())
ans = ""
while(n>0):
    ans = str(n%3) + ans
    n //= 3
print(ans)
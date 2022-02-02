#씨름선수(그리디)

n=int(input())
apply=[]

for _ in range(n):
    h,w=map(int,input().split())
    apply.append((h,w))

apply.sort(reverse=True)

largest=0
cnt=0
for h,w in apply:
    if largest<w:
        cnt+=1
        largest=w

print(cnt)
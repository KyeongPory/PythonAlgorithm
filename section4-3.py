n,m=map(int,input().split())
music=list(map(int,input().split()))

def Count(capacity):
    cnt=1
    sum=0
    for i in music:
        if sum+i>capacity:
            cnt+=1
            sum=i
        else:
            sum+=i
    return cnt

lt=1
rt=sum(music)
res=0
maxx=max(music)

while lt<=rt:
    mid=(lt+rt)//2
    if maxx<=mid and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1

print(res)
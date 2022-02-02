n,c=map(int,input().split())
li=[]

#이거 해결 못 함.
def Count(leng):
    cnt=1
    ep=li[0] #말의 배치 지점
    for i in range(1,n):
        if li[i]-ep>=leng:
            cnt+=1
            ep=li[i]
        
    return cnt

#주어진 리스트 한줄씩 받기
for _ in range(n):
    li.append(int(input()))

li.sort()

lt=1
rt=li[-1]
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        lt=mid+1
        res=mid
    else:
        rt=mid-1

print(res)
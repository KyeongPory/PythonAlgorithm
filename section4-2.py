k,n=map(int,input().split())
li=[]
largest=0

#가지고 있는 랜선을 리스트에 담으면서 최대길이의 랜선 찾기
for _ in range(k):
    a=int(input())
    li.append(a)
    if largest<a:
        largest=a

#자른 랜선의 개수 구하는 함수
def num(mid):
    cnt=0
    for i in li:
        cnt+=(i//mid)
    return cnt

lt=1
rt=largest
res=0

#자를 수 있는 최대 랜선 길이 구하기
while lt<=rt:
    mid=(lt+rt)//2
    if num(mid)<n:
        rt=mid-1
    else:
        lt=mid+1
        res=mid

print(res)
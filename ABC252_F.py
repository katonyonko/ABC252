import io
import sys

_INPUT = """\
6
5 7
1 2 1 2 1
3 1000000000000000
1000000000 1000000000 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop, heappush
  N,L=map(int,input().split())
  A=list(map(int,input().split()))
  if L>sum(A): A.append(L-sum(A))
  h=[]
  for i in range(len(A)):
    heappush(h,A[i])
  ans=0
  while len(h)>1:
    x=heappop(h)
    y=heappop(h)
    heappush(h,x+y)
    ans+=x+y
  print(ans)
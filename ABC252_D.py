import io
import sys

_INPUT = """\
6
4
3 1 4 1
10
99999 99998 99997 99996 99995 99994 99993 99992 99991 99990
15
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  A=list(map(int,input().split()))
  ans=N*(N-1)*(N-2)//6
  d=defaultdict(int)
  for i in range(N):
    d[A[i]]+=1
  for k in d:
    if d[k]>=2:
      ans-=d[k]*(d[k]-1)//2*(N-d[k])
    if d[k]>=3:
      ans-=d[k]*(d[k]-1)*(d[k]-2)//6
  print(ans)
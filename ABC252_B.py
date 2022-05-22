import io
import sys

_INPUT = """\
6
5 3
6 8 10 7 10
2 3 4
5 2
100 100 100 1 1
5 4
2 1
100 1
2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  B=set(list(map(int,input().split())))
  m=max(A)
  ans='No'
  for i in range(N):
    if A[i]==m and i+1 in B: ans='Yes'
  print(ans)
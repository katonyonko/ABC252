import io
import sys

_INPUT = """\
6
3
1937458062
8124690357
2385760149
5
0123456789
0123456789
0123456789
0123456789
0123456789
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N=int(input())
  S=[input() for _ in range(N)]
  ans=10**100
  for i in range(10):
    m=[S[j].index(str(i)) for j in range(N)]
    d=defaultdict(int)
    for j in range(N):
      d[m[j]]+=1
    tmp=max([k+(d[k]-1)*10 for k in d])
    ans=min(ans,tmp)
  print(ans)
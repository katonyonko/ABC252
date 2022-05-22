import io
import sys

_INPUT = """\
6
4
1 2 4 3
8
1 2 3 5 6 7 8 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  P=list(map(int,input().split()))
  mod=998244353
  dp=[[0]*N for _ in range(N)]
  for l in range(N):
    for i in range(N-l):
      if l==0: dp[i][i+l]=1
      else:
        for j in range(l):
          if P[i]<P[i+j+1]: continue
          dp[i][i+l]=(dp[i][i+l]+dp[i+1][i+j]*dp[i+j+1][i+l])%mod
        dp[i][i+l]=(dp[i][i+l]+dp[i+1][i+l])%mod
  print(dp[0][-1])
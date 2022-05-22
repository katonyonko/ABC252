import io
import sys

_INPUT = """\
6
3 3
1 2 1
2 3 2
1 3 10
4 6
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1
3 4 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  def Dijkstra(G,s):
    done=[False]*len(G)
    inf=10**20
    C=[inf]*len(G)
    C[s]=0
    h=[]
    heappush(h,(0,s))
    while h:
      x,y=heappop(h)
      if done[y]:
        continue
      done[y]=True
      for v in G[y]:
        if C[v[1]]>C[y]+v[0]:
          C[v[1]]=C[y]+v[0]
          heappush(h,(C[v[1]],v[1]))
    return C
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  d=dict()
  for i in range(M):
    A,B,C=map(int,input().split())
    A-=1; B-=1
    G[A].append((C,B))
    G[B].append((C,A))
    d[(min(A,B),max(A,B))]=i+1
  D=Dijkstra(G,0)
  used=set()
  que=[0]
  ans=[]
  while que:
    q=que.pop()
    used.add(q)
    for c,v in G[q]:
      if v in used: continue
      if D[v]==D[q]+c:
        ans.append(d[min(q,v),max(q,v)])
        que.append(v)
  print(*ans)
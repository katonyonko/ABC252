import io
import sys

_INPUT = """\
6
97
122
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  print(chr(N-97+ord('a')))
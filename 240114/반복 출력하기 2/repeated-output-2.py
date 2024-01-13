n = int(input())

def solution(n):
  if n == 0:
    return
  solution(n-1)
  print("HelloWorld")

solution(n)
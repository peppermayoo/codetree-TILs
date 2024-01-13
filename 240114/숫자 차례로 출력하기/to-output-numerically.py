n = int(input())

def solution(n):
    if n == 0:
        return
    solution(n-1)
    print(n, end= " ")

def solution2(n):
  if n == 0:
    return
  print(n, end=" ")
  solution2(n-1)

solution(n)
print()
solution2(n)
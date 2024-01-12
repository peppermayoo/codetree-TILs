def solution(x,y):
    max_num = max(x,y)
    min_num = min(x,y)
    if x == max_num:
      x = x + 25
    elif x == min_num:
      x = x * 2
    if y == max_num:
      y = y + 25
    elif y == min_num:
      y = y * 2
    return x,y

a,b = map(int,input().split())
changed_a, changed_b = solution(a,b)
print(changed_a, changed_b)
def solution(x,y):
    max_num = max(x,y)
    min_num = min(x,y)
    x = max_num+25
    y = min_num*2
    return x,y

a,b = map(int,input().split())
changed_a, changed_b = solution(a,b)
print(changed_b,changed_a)
a,b = map(int,input().split())

def solution(x,y):
    max_num = max(x,y)
    min_num = min(x,y)
    if x == max_num:
        x = max_num*2
    elif x == min_num:
        x = min_num+10
    if y == max_num:
        y = max_num*2
    elif y == min_num:
        y = min_num+10
    return x,y

ans = solution(a,b)
for ele in ans:
    print(ele, end=" ")
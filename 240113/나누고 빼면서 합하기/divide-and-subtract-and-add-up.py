def solution(x,y,z):
    cnt = 0
    while y:
        cnt += z[y-1]
        if y%2 != 0:
            y -= 1
        else:
            y //= 2

    return cnt

n,m = map(int,input().split())
a = list(map(int,input().split()))
print(solution(n,m,a))
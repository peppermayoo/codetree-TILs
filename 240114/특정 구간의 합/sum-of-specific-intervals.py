n,m = map(int,input().split())
n_list = list(map(int,input().split()))

def solution(n,m,a1,a2):
    return sum(n_list[a1-1:a2])

for _ in range(m):
    a1,a2 = map(int,input().split())
    print(solution(n,m,a1,a2))
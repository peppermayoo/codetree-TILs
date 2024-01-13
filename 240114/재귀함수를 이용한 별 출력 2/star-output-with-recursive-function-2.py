n = int(input())

def solution(n):
    if n == 0:
        return
    print('* '*n)
    solution(n-1)
    print('* '*n)

solution(n)
def solution(a):
    for i in range(len(a)):
        a[i] = abs(a[i])
    return a

n = int(input())
n_list = list(map(int, input().split()))
n_list = solution(n_list)

for ele in n_list:
    print(ele, end=" ")
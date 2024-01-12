a = input()

def solution(x):
    a_list = []
    for i in range(len(x)):
        a_list.append(x[i])
    ans = set(a_list)
    if len(ans) >= 2:
      return 'Yes'
    return 'No'

print(solution(a))
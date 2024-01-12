def solution(a):
  b = []
  for i in range(len(a)):
    b.append(a[i])
  return b[::-1]

def check(a):
  a_list = []
  b_list = solution(a)
  for j in range(len(a)):
    a_list.append(a[j])

  if a_list == b_list:
    return 'Yes'
  return 'No'

a = str(input())
solution(a)
print(check(a))
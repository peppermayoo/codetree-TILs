n = int(input())

def solution(n):
    if n < 10:
        return n**2 
    return solution(n//10)+(n%10)**2 

print(solution(n))
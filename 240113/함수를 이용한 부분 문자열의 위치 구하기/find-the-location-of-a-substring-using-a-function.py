a = input()
b = input()

def solution(x,y):
    if y in x:
        for i in range(len(x)):
            if x[i:i+len(y)+1] == y:
                return i 
    return -1
            
print(solution(a,b))
def solution(ineq, eq, n, m):
    answer = 0
    ieg = ineq+eq.replace('!','')
    if int(eval(str(n)+ieg+str(m))) == True:
        answer = 1
    else:
        answer = 0
    return answer
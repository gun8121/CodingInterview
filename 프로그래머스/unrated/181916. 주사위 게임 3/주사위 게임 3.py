def solution(a, b, c, d):
    dice = [a,b,c,d]
    counts = [dice.count(i) for i in dice]
    answer = 0
    if max(counts) == 4:
        answer = 1111 * a
    elif max(counts) == 3:
        p = dice[counts.index(3)]
        q = dice[counts.index(1)]
        answer = (10*p+q)**2
    elif max(counts) == 2:
        if min(counts) == 2:
            if a == b:
                answer = (a+c) * abs(a-c)
            else:
                answer = (a+b) * abs(a-b)
        else:
            p = dice[counts.index(2)]
            answer = (a*b*c*d)/(p*p)
    else:
        answer = min(dice)
    return answer

# 4 주사위 모두 p로 같다면 -> 1111 x p
# 3 주사위 p로 같고 나머지 숫자 q -> (10*p+q)^2
# 2 주사위 p 2 주사위 q -> (p+q) x |p-q|
# 2 주사위 p 1 주사위 q 1 주사위 r -> q*r
# 4 주사위 모두 다름 -> 가장 작은 숫자 만큼 점수
def solution(money):
    answer = []
    cnt = 0
    for i in range(182):
        if money >= 5500:
            money -= 5500
            cnt += 1
    answer = [cnt, money]
    return answer
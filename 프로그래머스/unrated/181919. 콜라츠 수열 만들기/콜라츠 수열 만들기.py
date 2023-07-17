def solution(n):
    answer = []

    while n != 1:
        answer.append(int(n))
        if n%2==0:
            n = n / 2
        else:
            n = n *3 + 1
    answer.append(1)
    return answer

# 반복문 n이 1이 될 때 까지 반복해서 연산을 수행
# 변경된 n 의 값을 리스트에 저장
def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer

# l 과 r 사이에 "0" 과 "5" 로 이루어진 정수 찾기
# all() 내장함수 사용
# 오름차 순
# answer 길이가 0 이면/ 없다면 "-1" 담긴 배열 리턴
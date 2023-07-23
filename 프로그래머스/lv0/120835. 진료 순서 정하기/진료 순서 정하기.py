def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True) # 응급도가 높은 순서대로 정렬
    answer = [sorted_emergency.index(x)+1 for x in emergency] # 응급도가 높은 순서대로 번호 부여
    return answer
def solution(numbers, k):
    idx = 0  # 현재 던지는 사람의 인덱스
    for i in range(k-1):
        # 오른쪽으로 한 명 건너뛴다
        idx = (idx + 2) % len(numbers)
    return numbers[idx]
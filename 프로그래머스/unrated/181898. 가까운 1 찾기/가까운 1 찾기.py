def solution(arr, idx):
    answer = -1
    for i, val in enumerate(arr):
        if idx <= i and val == 1:
            return i
    return answer
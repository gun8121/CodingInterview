def solution(arr, intervals):
    answer = []
    for idx, val in enumerate(intervals):
        s, e = val
        answer += arr[s:e+1]
    return answer
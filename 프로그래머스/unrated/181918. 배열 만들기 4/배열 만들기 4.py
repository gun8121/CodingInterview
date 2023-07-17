# arr 이용해 stk 배열 만들기
# 변수 i를 0으로 설정후 i가 arr 의 길이보다 작으면...
# 1. if stk is empty.. add arr[i] to stk and i + 1
# 2. stk not empty, stk last element smaller than arr[i], add arr[i] to end of stk
# 3. stk not empty, stk last element bigger or equal to arr[i], remove last element of stk
# return stk

def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] >= arr[i]:
            stk.pop()
    return stk
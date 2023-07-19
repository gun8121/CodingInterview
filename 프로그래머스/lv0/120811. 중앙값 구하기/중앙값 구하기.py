import math

def solution(array):
    answer = 0
    array.sort()
    tmp = math.ceil(len(array)/2)
    answer = array[tmp-1]
    return answer
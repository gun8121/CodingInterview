def solution(number):
    answer = 0
    number_list = [int(i) for i in number]
    sumss = sum(number_list)
    answer = sumss%9
    return answer
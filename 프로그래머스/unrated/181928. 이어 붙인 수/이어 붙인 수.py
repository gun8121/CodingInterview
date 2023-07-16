def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for i, val in enumerate(num_list):
        if val%2==1:
            odd = odd + str(num_list[i])
        else:
            even = even + str(num_list[i])
    answer = int(odd) + int(even)
    return answer
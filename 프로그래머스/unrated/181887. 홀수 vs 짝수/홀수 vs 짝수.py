def solution(num_list):
    answer = 0
    ans_even = 0
    ans_odd = 0
    for idx, val in enumerate(num_list):
        if idx%2==0:
            ans_odd += val
        elif idx%2!=0:
            ans_even += val
    if ans_even > ans_odd:
        answer = ans_even
    else:
        answer = ans_odd
    return answer
def solution(arr, queries):
    for s,e,k in queries:
        for i in range(s, e+1):
            if i%k==0:
                arr[i] += 1   
    return arr


# def solution(arr, queries):
#     result = []
#     for q in queries:
#         s,e,k = q
#         answer = []
#         for i in arr[s:e+1]:
#             if i > k:
#                 answer.append(i)
#         if not answer:
#             result.append(-1)
#         else:
#             result.append(min(answer))
#     return result
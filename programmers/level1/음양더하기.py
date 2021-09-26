def solution(absolutes, signs):
    sign_arr = [-1, 1]
    return sum(absolutes[i] * sign_arr[signs[i]] for i in range(len(absolutes)))
def solution(numbers):
    result = []
    
    for num in numbers:
        bin_num = list('0' + bin(num)[2:])
        for i in range(len(bin_num) - 1, -1, -1):
            if bin_num[i] == '0':
                bin_num[i] = '1'
                if i != len(bin_num) - 1:
                    bin_num[i+1] = '0'
                break
        result.append(int("".join(bin_num), 2))
    return result
def solution(s):
    n = len(s)
    answer = n
    
    for c in range(1, n//2+1):
        compressed = ""
        i = 0
        j = i + c
        while i + c <= n:
            count = 1
            while j + c <= n and s[i:i+c] == s[j:j+c]:
                count += 1
                j += c
            if count > 1:
                compressed += str(count)
            compressed += s[i:i+c]
        
            i = j
            j += c
        if i < n:
            compressed += s[i:]
        answer = min(answer, len(compressed))
    return answer

print(solution("abcdefg"))
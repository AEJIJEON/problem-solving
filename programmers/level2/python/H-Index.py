from bisect import bisect_left
    
def solution(citations):
    citations.sort()

    for h in range(citations[-1], -1, -1):
        if len(citations) - bisect_left(citations, h) >= h:
            
            return h
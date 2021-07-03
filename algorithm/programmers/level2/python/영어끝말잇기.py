def solution(n, words):

    for i, word in enumerate(words):
        if word in word[:i] or (i > 0 and words[i-1][-1] != word[0]):
            return [i % n + 1, i//n + 1]
    return [0, 0]
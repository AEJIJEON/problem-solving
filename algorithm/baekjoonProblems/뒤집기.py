s = input()
count = [0, 0]
for i in range(len(s)):
    if i == len(s) - 1  or s[i] != s[i + 1]:
        count[int(s[i])] += 1
    
print(min(count))


# 개선
s = input()
count = 0
for i in range(len(s)):
    if i == len(s) - 1  or s[i] != s[i + 1]:
        count += 1
    
print(count // 2)
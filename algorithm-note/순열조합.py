from itertools import combinations, permutations

lst = [1, 2, 3]
perm = list(permutations(lst))
# combinations ftn에서 r값 필수!
comb = list(combinations(lst, len(lst)))

print(perm, comb)

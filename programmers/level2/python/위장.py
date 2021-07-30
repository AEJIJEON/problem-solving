# 딕셔너리를 선언하여 종류: [이름1, 이름2, ...]와 같은 key: value 형태로 저장한다.
# 의상의 종류가 총 n가지, n가지 종류에 대한 각 의상의 수가 x1, x2, ..., xn이라고 할 때 
# 서로 다른 옷의 조합의 수 = (x1 + 1) * (x2 + 1) * ... * (xn + 1) - 1
# -1을 해주어 아무 의상도 입지 않은 경우를 제외시켰다.

def solution(clothes):
    cloth_dic = dict()
    for cloth, kind in clothes:
        if kind not in cloth_dic:
            cloth_dic[kind] = 1
        else:
            cloth_dic[kind] += 1
    
    result = 1
    for value in cloth_dic.values():
        result *= value + 1
    
    return result - 1
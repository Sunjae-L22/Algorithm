# from typing import List
#
# class RESULT:
#     def __init__(self, mHeights : List[List[int]]):
#         self.heights = mHeights
#
# def init(N : int, M : int, mIceBlock : List[List[int]], mIceGroup : List[List[int]]) -> None:
#     pass
#
# def oneYearLater() -> RESULT:
#     res = RESULT([[0 for _ in range(100)] for _ in range(100)])
#     return res
END = "$"          # 단어의 끝을 나타내는 특별한 키

def build(words):
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})   # 없으면 {} 를 만들고, 있으면 그걸 반환
        node[END] = True                     # 여기서 단어가 끝난다
    return root

root = build(["cat", "car", "card", "dog"])
print(root)
from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    failer = list(diff.elements())
    return failer[0]

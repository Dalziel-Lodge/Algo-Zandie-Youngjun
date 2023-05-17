def solution(participant, completion):
    hash_dict = {}
    sum_hash = 0

    for p in participant:
        hash_dict[hash(p)] = p
        sum_hash += hash(p)

    for c in completion:
        sum_hash -= hash(c)

    return hash_dict[sum_hash]

#해시로 풀기. 딕셔너리의 키값을 해시값을 만들어서 담고
#해시값을 빼가면서 남은 해시값에 해당하는 놈 찾기
#단 한명의 선수를 제외하고는 모든 선수가 마라톤을 완주했음, 문제 잘 읽기

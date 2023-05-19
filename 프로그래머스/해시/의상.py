def solution(clothes):

    answer = 1
    hash_map = {}

    for item in clothes:
        if item[1] in hash_map:
            hash_map[item[1]].append(item[0])
        else:
         hash_map[item[1]] = [item[0]]

    for key in hash_map.keys():
        answer = answer*(len(hash_map[key])+1)

    return answer-1


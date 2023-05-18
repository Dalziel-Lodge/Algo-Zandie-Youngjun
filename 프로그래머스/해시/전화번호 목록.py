def solution(phone_book):
    hash_map = {}
    answer = True
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        prefix = ""
        for number in phone_number:
            prefix += number
            if prefix in hash_map and prefix != phone_number:
                answer = False
    return answer

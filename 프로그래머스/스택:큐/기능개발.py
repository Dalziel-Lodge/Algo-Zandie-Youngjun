def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        work = 100 - progresses[i]
        day = work // speeds[i]
        if work % speeds[i] != 0:
            day += 1
        days.append(day)

    count = 0
    max_day = days[0]

    for day in days:
        if day > max_day:
            answer.append(count)
            max_day = day
            count = 1
        else:
            count += 1

    # 3 2 1 3 4
    answer.append(count)

    return answer

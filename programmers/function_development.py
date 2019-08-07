def solution(progresses, speeds):
    answer = []

    days = 0
    index = 0
    while progresses:
        # 작업률이 100보다 크면 배포될 작업이므로 값을 계속 증가 시켜준다.
        if progresses[0] + (days * speeds[0]) >= 100:
            answer[index] += 1
        else:
            days = find_complete_day(days, speeds[0], progresses[0])
            index = len(answer)
            answer.append(1)

        progresses.pop(0)
        speeds.pop(0)

    return answer


# 값이 100보다 작으면 배포될 시점까지 작업률을 증가시킨다.
def find_complete_day(days, speed, progress):
    while progress + (days * speed) < 100:
        days = days + 1

    return days
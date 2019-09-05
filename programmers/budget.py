def solution(budgets, M):
    answer = max(budgets)

    def get_sum(limit):
        result = 0
        for b in budgets:
            result += limit if b > limit else b

        return result

    total = sum(budgets)
    if total <= M:
        return answer

    answer = int((min(budgets) + answer)/4)
    total = get_sum(answer)

    if total < M:
        while total <= M:
            answer += 1
            total = get_sum(answer)
        answer -= 1

    else:
        while total >= M:
            answer -= 1
            total = get_sum(answer)
        answer += 1

    return answer


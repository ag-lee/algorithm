
def solution(n):
    # 3진수를 1,2,4를 이용해 표현한다.
    # 1: 1 / 2: 2 / 0: 4
    answer = ''

    while n:
        n, remainder = divmod(n, 3)

        answer = str(remainder) + answer
        if remainder == 0:
            n -= 1

    answer = answer.replace('0', '4')
    return answer
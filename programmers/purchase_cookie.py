def solution(cookie):
    answer = 0

    n = len(cookie)

    def is_in_range(l, r):
        if l > m or r <= m:
            return False
        return True

    # m 값에 대해 가장 큰 쿠키 갯수를 찾는다.
    def find_max_cookie(m):
        l = 0
        r = n - 1

        # 0 ~ m, m+1 ~ n-1까지 쿠키 갯수를 더한다.
        l_sum = sum(cookie[l: m + 1])
        r_sum = sum(cookie[m + 1: r + 1])

        # 쿠키 개수가 다르면 더 큰 값을 가진 쿠키 개수를 1단계 감소시킨다.
        while l_sum != r_sum and is_in_range(l, r):
            if l_sum > r_sum:
                l_sum -= cookie[l]
                l += 1
            else:
                r_sum -= cookie[r]
                r -= 1

        if l_sum == r_sum:
            return l_sum
        else:
            return 0

    # 1 ~ n까지 m을 정해 가장 큰 값을 찾는다.
    for m in range(n):
        new_answer = find_max_cookie(m)
        if answer < new_answer:
            answer = new_answer

    return answer

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        # 스킬트리에 포함된 문자들의 index들을 배열에 저장한다.
        indexes = []

        for s in skill:
            i = skill_tree.find(s)
            if i != -1:
                indexes.append(i)
            else:
                # 유저들의 스킬트리에 포함되지 않은 경우 MAX INDEX인 26보다 큰 27을 넣어준다.
                indexes.append(27)

        # 정렬된 것과 정렬되지 않은 것이 일치한다면, 정상적인 스킬트리이다.
        if sorted(indexes) == indexes:
            answer += 1

    return answer

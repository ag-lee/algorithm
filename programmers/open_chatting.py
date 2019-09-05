def solution(record):
    answer = []

    user_info = {}

    # get user info (uid, nickname)
    for r in record:

        if "Leave" not in r:
            tokens = r.split(" ");
            user_info[tokens[1]] = tokens[2]

    # make answers
    for r in record:
        tokens = r.split(" ");
        if "Enter" == tokens[0]:
            answer.append(user_info[tokens[1]] + "님이 들어왔습니다.")
        elif "Leave" == tokens[0]:
            answer.append(user_info[tokens[1]] + "님이 나갔습니다.")

    return answer
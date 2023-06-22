def solution(record):
    answer = []
    user = {}

    for log in record:
        split_data = log.split(' ')
        if split_data[0] == 'Enter':
            user[split_data[1]] = split_data[2]
            answer.append([f'{split_data[1]}', '님이 들어왔습니다.'])

        if split_data[0] == 'Leave':
            answer.append([f'{split_data[1]}', '님이 나갔습니다.'])

        if split_data[0] == 'Change':
            user[split_data[1]] = split_data[2]

    return [user[key] + p for key, p in answer]
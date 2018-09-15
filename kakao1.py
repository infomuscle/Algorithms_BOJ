record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def solution(record):
    idNname = {}

    for i in range(len(record)):
        box = record[i].split()
        if len(box) == 3:
            # cmd = box[0]
            id = box[1]
            nickname = box[2]
            # if cmd == "Enter":
            idNname[id] = nickname
            # elif cmd == "Change":
            #     idNname[id] = nickname
        elif len(box) == 2:
            # cmd = box[0]
            id = box[1]
            # if cmd == "Leave":
            del idNname[id]

    answer = []

    for i in range(len(record)):
        box = record[i].split()
        cmd = box[0]
        id = box[1]

        if cmd == "Enter":
            answer.append(idNname[id] + "님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(idNname[id] + "님이 나갔습니다.")

    return answer

print(solution(record))

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
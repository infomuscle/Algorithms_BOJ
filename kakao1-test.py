record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Change uid4567 Ryan"]


ids = []
nicknames = []
idNname = {}

for i in range(len(record)):
    cmd = record[i][:5]
    id = record[i][6:13]
    nickname = record[i][14:]
    if cmd == "Enter":
        idNname[id] = nickname
    elif cmd == "Leave":
        del idNname[id]
    elif cmd == "Chang":
        idNname[record[i][7:14]] = record[i][15:]

print(idNname)

printBox = []

for i in range(len(record)):
    cmd = record[i][:5]
    id = record[i][6:13]
    if cmd == "Enter":
        printBox.append(idNname[id]+"님이 들어왔습니다.")
    elif cmd == "Leave":
        printBox.append(idNname[id]+"님이 나갔습니다.")

print(printBox)

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
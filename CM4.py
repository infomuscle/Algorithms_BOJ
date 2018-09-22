# def treeTraverser(N, directory, query):
#     cnt = 1
#     answer = []
#     idx = 0
#     for i in range(idx, N-1):
#         if directory[i][0] == query[0]:
#             if directory[i][1] == query[1]:
#                 cnt += 1
#                 answer.append(cnt)
#                 return answer
#             else:
#                 idx += 1
#                 now = [directory[i][1], query[1]]
#                 treeTraverser(idx, now, query)

def treeTraverser(N, directory, query, cnt):
    for i in range(N-1):
        if directory[i][0] == query[0]:
            if directory[i][1] == query[1]:
                cnt += 1
                return cnt
            else:
                now = [directory[i][1], query[1]]
                # directory.remove(directory[i])
                treeTraverser(N-1, directory, now, cnt+1)
        elif directory[i][1] == query[0]:
            now = [directory[i][0], query[1]]
            # directory.remove(directory[i])
            treeTraverser(N-1, directory, now, cnt+1)


def solution(N, directory, query):
    answer = []
    for i in range(len(query)):
        answer.append(treeTraverser(N, directory, query[i], 1))

    return answer

d1 = [[1,2], [1,3], [2,4], [2,5]]
q1 = [[1,5], [2,5], [3,5],[4,5]]
d2 = [[3,2], [3,1], [3,4]]
q2 = [[3,1]]

# print(treeTraverser(5, d1, q1, 1))
print(solution(5, d1, q1))
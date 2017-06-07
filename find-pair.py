def solution(A):
    lookFor = set()
    for a in A:
        if a in lookFor:
            lookFor.remove(a)
        else:
            lookFor.add(a)
    return lookFor.pop()

result = solution([9, 3, 9, 3, 9, 7, 9])
print(result)

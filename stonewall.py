def solution(H):
    N = len(H)
    current = [0] * N
    current_index = 0
    blocks = 0
    for i in range(N):
        if H[i] == 0:
            current_index = 0
        else:
            if current_index == 0:
                current[current_index] = H[i]
                current_index += 1
                blocks += 1
            elif H[i] == current[current_index-1]:
                continue
            elif H[i] < current[current_index-1]:
                while current_index > 0 and H[i] < current[current_index-1]:
                    current_index -= 1
                if H[i] > current[current_index-1]:
                    current[current_index] = H[i]
                    current_index += 1
                    blocks += 1
            else:
                current[current_index] = H[i]
                current_index += 1
                blocks += 1
    return blocks

H = [0] * 9
H[0] = 8
H[1] = 8
H[2] = 5
H[3] = 7
H[4] = 9
H[5] = 8
H[6] = 7
H[7] = 4
H[8] = 8
# expected result: 7

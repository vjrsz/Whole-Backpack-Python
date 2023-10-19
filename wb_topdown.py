global M


def wb_recursive_topdown(n, w, v, W):
    pass


def wb_topdown(n, w, v, W):
    global M
    M = [[0] * W] * n

    for x in range(0, W):
        M[0][x] = 0
        for j in range(1, n):
            M[j][x] = 0
            M[j][0] = 0
    return wb_recursive_topdown(n, w, v, W)


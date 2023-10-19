def wb(n, w, v, W):
    if n == 0 or W == 0:
        return -0

    if w[n] > W:
        return wb(n - 1, w, v, W)
    else:
        use = v[n] + wb(n - 1, w, v, W - w[n])
        no_use = wb(n - 1, w, v, W)

        return max(use, no_use)
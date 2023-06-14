import sys

input = sys.stdin.readline
MAX = 1000000000

def f(frm, to):
    if frm == to:
        return histograms[frm]

    mid = (frm + to) // 2
    l = f(frm, mid)
    r = f(mid + 1, to)

    max_val = max(l, r)

    h = min(histograms[mid], histograms[mid + 1])
    w = 2
    s = w * h
    i, j = mid, mid + 1
    while frm < i or j < to:
        if j == to or frm < i and histograms[i - 1] >= histograms[j + 1]:
            i -= 1
            w += 1
            h = min(h, histograms[i])
            s = max(s, w * h)
        else:
            j += 1
            w += 1
            h = min(h, histograms[j])
            s = max(s, w * h)

    max_val = max(max_val, s)

    return max_val


while True:
    inp = list(map(int, input().split()))
    n = inp[0]
    if n == 0:
        break
    histograms = inp[1:]

    print(f(0, len(histograms) - 1))
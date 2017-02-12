
def maximum(a):
    assert len(a) > 0

    # best = a[0]
    best = 0
    for x in a:
        if x > best:
            best = x
    return best

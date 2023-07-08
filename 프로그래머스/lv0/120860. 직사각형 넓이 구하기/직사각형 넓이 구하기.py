def solution(dots):
    ax,ay = 256,256
    bx,by = -256,-256
    for x, y in dots:
        ax = min(ax, x)
        ay = min(ay, y)
        bx = max(bx, x)
        by = max(by, y)
        
    return (ax-bx) * (ay-by)
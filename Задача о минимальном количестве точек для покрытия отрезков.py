def key(short):
    return short[1]

def points(N,shorts):
    shorts = list(shorts)
    shorts.sort(key = key)
    i,k = 0,0
    point = []
    while i<N:
        if shorts[k][1]<shorts[i][0]:
            point.append(shorts[k][1])
            k=i
        elif shorts[k][1]>=shorts[i][0]:
            if i==N-1:
                point.append(shorts[k][1])
            i+=1
    print(len(point))
    print(" ".join(str(e) for e in point))
    return point

if __name__=='__main__':
    N = int(input())
    shorts = []
    for i in range(N):
        shorts.append(tuple(map(int,input().split(' '))))
    points(N,shorts)
def key(item):
    item[0]=item[0]/item[1]
    return item[0]

def robbing(N,W,items):
    items.sort(key=key,reverse=True)
    rucksack = 0
    for i in range(N):
        rucksack+=min(W,items[i][1])*items[i][0]
        W-=min(W,items[i][1])
        if W==0:
            break
    print("%.3f" % rucksack)
    return rucksack

if __name__=='__main__':
    N,W = tuple(map(int,input().split(' ')))
    items = []
    for i in range(N):
        items.append(list(map(int,input().split(' '))))
    robbing(N,W,items)
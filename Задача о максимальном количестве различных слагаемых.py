def terms(N):
    numbers = []
    for i in range(0,N+1):
        if N-i<i+1 or (N-i)==i:
            numbers.append(N)
            N-=N
        else:
            numbers.append(i)
            N-=i
            i+=1
            continue
        if N==0:
            break
    print(len(numbers)-1)
    print(" ".join(str(number) for number in numbers[1:]))


if __name__=='__main__':
    N=int(input())
    terms(N)
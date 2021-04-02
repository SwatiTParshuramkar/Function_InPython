def aVeryBigSum(ar):
    i=0
    sum1=0
    while i < len(ar):
        sum1+=ar[i]
        i+=1
    return sum1

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)

def printAverage(arr):
    b=0
    summ=0
    while b<len(arr):
        if len(arr)>0:
            summ+=arr[b]
            b+=1
            print(summ//len(arr))
        if len(arr)==0:
            print(0)
 






def bubleSort(n):
    print("Original List is =>",n)
    i=0
    while i<len(n):
        j=0
        while j<(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
            j+=1
        i+=1
        
n=[20,40,5,34,12,50,16,35]
bubleSort(n)

i=0
buble_Sort=[]
while i<len(n):
    buble_Sort.append(n[i])
    i+=1

print("Buble Sort List is =>", buble_Sort)
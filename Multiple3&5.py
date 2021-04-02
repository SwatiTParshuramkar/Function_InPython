def showNumbers(limit):
    i=0
    sum=0
    while i <= limit :
        if i%3==0 or i%5==0 :
            sum+=i
        i+=1
    print(sum)
    
number=int(input("Enter the limit"))
showNumbers(number)
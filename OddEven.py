def showNumbers(limit):
    i=0
    while i <= limit :
        if i%2==0:
            print(i,"Even")
        else:
            print(i,"Odd")
        i+=1
number=int(input("Enter the limit"))
showNumbers(number)
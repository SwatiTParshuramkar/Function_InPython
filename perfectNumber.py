def perfect_num(number):
    s=0
    i=1
    while i < n :
        if n%i ==0 :
            s=s+i
        i+=1
    
    if s != n :
        print("Not perfect number")
    else :
        print("perfect number")
    
n=int(input("Enter the num"))
perfect_num(n)
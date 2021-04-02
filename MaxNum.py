# i=0
def maximum():
    i=0
    max=number[0]
    while i<len(number):
        m=number[i]
        if m>max:
            max=m
        i+=1
    print("Maximum number is",max)

number=[10,20,30,40,70,60]    

maximum()

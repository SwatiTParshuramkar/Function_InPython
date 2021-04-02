def change_list(a,b,multiply):
    i=0
    mul=0
    list3=[]
    while i < len (a):
        mul = list1[i] * list2[i]
        list3.append(mul)
        i+=1
    return list3

list1 = [5, 10, 50, 20]
list2 =  [2, 20, 3, 5]

print(change_list(list1,list2,"multiply"))
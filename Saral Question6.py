def list_change(multiple_list):
    i=0
    while i< len (multiple_list):
        j=0
        b=[]
        while j< len(multiple_list[i][j]):
                c =(multiple_list[i][j]) *( multiple_list[i][j])
                b.append(c)
                j+=1
        i+=1
        return b
        
    
    
    


multiple_list = list_change([[5, 10, 50, 20], [2, 20, 3, 5]])
print(multiple_list)

def linearSearch(arr=[0,0],key=0):
    for k in range(0,len(arr),1):
        if arr[k]==key:
            print(k)
            return k
        else:  
            k=None

        
print(linearSearch([12,2,5,8,3,90],910))
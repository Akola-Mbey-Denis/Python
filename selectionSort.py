def selectionSort(list):
    for i in range(0,len(list)-1):
        for k in range(len(list)-1,i,-1):
            if list[i]>list[k]:
                temp=list[i]
                list[i]=list[k]
                list[k]=temp
    return list

print(selectionSort([12,90, 12,12,450,45,123,123]))
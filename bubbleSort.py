def bubbleSort(list):
    swap=False
    for k in range(1,len(list)):
          if list[k-1]>list[k]:
            swap=True
            temp=list[k]
            list[k]=list[k-1]
            list[k-1]=temp
            bubbleSort(list) 
          else:
              swap=False
    if swap==False:
        return list
print(bubbleSort([12, 16,78,0,5,2,3,3,2]))
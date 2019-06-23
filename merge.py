def mergeSorting(array):
    if len(array)>1:
        mid=len(array)//2
        lowerPart= array[:mid]

        higherPart=array[mid:]

        mergeSorting(lowerPart)
        mergeSorting(higherPart)

        i=j=k=0
        while i<len(lowerPart) and j<len(higherPart):
            if lowerPart[i]<higherPart[j]:
                array[k]=lowerPart[i]
                i+=1
            
            else:
                array[k]=higherPart[j]
                j+=1
            k+=1
        while i<len(lowerPart):
            array[k]=lowerPart[i]
            i+=1
            k+=1
        while j<len(higherPart):
            array[k]=higherPart[j]
            j+=1
            k+=1
        return array
print(mergeSorting([1,100,34,56,78,450,2,4,90]))
    

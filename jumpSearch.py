import math
def jumpsearch(arr,key):
    keyValue=0
    step=int(math.sqrt(len(arr)))
    for k in range(step,len(arr),step):
         if arr[k]==key:#Check if the jumped key matches the searched item
            keyValue=key 
            #If the matched item is greater than the  item we search for
            # ,move backwards sequentially in steps of one to search for the  item
         elif arr[k]>key:
            for i in range(k-1,k-(step+1),-1):
                if arr[i]==key:
                    keyValue=i
            #If the matched item is less than the key,
            # we search linearly award and search for the item linearlly
         elif arr[k]<key:
            for x in range(k+1,len(arr),1):
                if arr[x]==key:
                    keyValue=x
    return keyValue
print(jumpsearch([12,13,25,28,29,45,78,85,91,100,111],100))




import time
def binarySearch(listSort=[0,0],key=0):
    low_index=0;
    high_index=len(listSort)-1
    mid_index=int((low_index+high_index)/2)
    
    while low_index<high_index:
        for k in range(0,len(listSort)):
            if listSort[k]>key:
                low_index=mid_index+1
            elif listSort[k]<key:
                high_index=mid_index-1

            elif listSort[k]==key:
                return k
            else:
                return "NOT FOUND!"
        mid_index=int((low_index+high_index)/2)



def interface(listSort,key):
    for i in range (0,len(listSort)-1):
         
            if listSort[i]>listSort[i+1]:
             
                answer =int(input("Do you wish to sort the list before sorting: Enter 1  to sort or 2 to proceed without sorting"))
                
                if answer==1:
                    listSort.sort(key=None,reverse=False)
                    print(listSort)
                elif answer==2:                            
                    print("proceeding")
                    break
    start_time= time.time()
    index=binarySearch(listSort,key)
    end_time=time.time()
    print("The index of the search item is :",index," The runtime of the sort is :",end_time-start_time)

interface([12,23,45,67,90,11,2],45)
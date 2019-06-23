import time
def sortalg(list):
    temp=0
   # int i=0
    for i in range (0,len(list)):
        for k in range (0,i):
            if list[i]<list[k]:
                temp=list[i]
                list[i]=list[k]
                list[k]=temp

                 
    return list
start_time=time.time()

print(sortalg([12,67,15,89,0,90,100,105]))
end_time=time.time()
print("Time of execution ",end_time-start_time)
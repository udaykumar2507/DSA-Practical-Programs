arr=[5,4,3,2,1]
for i in range(len(arr)):
    min_ind=i
    for j in range(i,len(arr)):
        if arr[j]<=arr[min_ind]:
            min_ind=j
    arr[min_ind],arr[i]=arr[i],arr[min_ind]
print(arr)
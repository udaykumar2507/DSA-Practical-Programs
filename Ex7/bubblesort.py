arr=[5,4,3,2,1]
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        arr[j]>arr[j+1]
        arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
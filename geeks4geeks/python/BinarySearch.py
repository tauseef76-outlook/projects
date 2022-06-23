def binarySearch(arr,l,h,ele):
        mid = h//2
        if(ele == arr(mid)):
            return (mid)
        elif(ele < arr[mid]):
            binarySearch(arr,l,mid-1,ele)
        elif(ele > arr[mid]):
            binarySearch(arr,mid+1,h,ele)
        else:
            return -1

arr = [2, 3, 4, 10, 40]
x = 10
l = 0
x = 10
h = len(arr)
res = binarySearch(arr,l,h,x)

print(res,"=======")


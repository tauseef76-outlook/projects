def binarySearch(arr, l, h, ele):
    if l > h:
        return -1
    mid = (l+h)//2
    if(ele == arr[mid]):
        return (mid+1)
    elif(ele < arr[mid]):
        binarySearch(arr, l, mid-1, ele)
    elif(ele > arr[mid]):
        binarySearch(arr, mid+1, h, ele)
    else:
        return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    res = binarySearch(arr,0,len(arr), 4)

    print(res, "=======")

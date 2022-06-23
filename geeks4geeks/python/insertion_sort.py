def insertion_sort(arr):
    for i in range(1,len(arr)):
        anchor = arr[i]
        j = i-1
        while j>=0 and anchor<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = anchor

if __name__ == "__main__":
    arr = [29,11,2,37,15,6,22]
    insertion_sort(arr)
    print(arr)

    test = [
        [23,2121,22,134,0,12],[0,22,1,3,5,1],[],[2]
    ]

    for elements in test:
        insertion_sort(elements)
        print(f"sorted arr: {elements}")

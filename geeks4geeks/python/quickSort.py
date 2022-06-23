def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

def partition(arr,low,high):
    pivot_index = low
    pivot = arr[pivot_index]

    while(low<high):

        while(arr[high] > pivot):
            high-=1

        while (arr[low] <= pivot and low<len(arr)):
            low += 1

        if(low<high):
            swap(arr,low,high)

    swap(arr,pivot_index,high)
    return 0

def swap(arr,a,b):
    arr[a],arr[b] = arr[b],arr[a]


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
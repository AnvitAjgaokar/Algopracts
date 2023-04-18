main_arr=[]

# Taking input Array from the user

in1 = int(input("Enter the length of the Array you want to Sort: "))

for i in range(in1):
    in2 = int(input("Enter your Element: "))
    main_arr.append(in2)

# Creating function for Quick sort
def quick_sort(arr,left,right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

# Creating function for partition
def partition(arr,left,right):
    i = left
    j = right -1
    pivot = arr[right]

    while i < j:
        # checking for the element at index i
        while i < right and arr[i] < pivot:
            i += 1

        # checking for the element at index j
        while j > left and arr[j] > pivot:
            j -= 1

        # Swapping elements at i and j index
        if i < j:
            (arr[i],arr[j]) = (arr[j],arr[i])

    # Swapping elemnet at i with the pivot element
    if arr[i] > pivot:
        (arr[i],arr[right]) = (arr[right],arr[i])

    return i

#driver code
print("The array before sorting is: ", main_arr,"\n")

quick_sort(main_arr,0,len(main_arr)-1)
print("The array after sorting is: ",main_arr)






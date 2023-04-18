#merge sort

main_arr=[]

# Taking input Array from the user

in1 = int(input("Enter the length of the Array you want to Sort: "))

for i in range(in1):
    in2 = int(input("Enter your Element: "))
    main_arr.append(in2)

# Creating Function for the merge sort
def merge_sort(arr):
    if len(arr) > 1:
        # Initialization of left and Right Array
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # Making the Recursion call on left and right array(divide)
        merge_sort(left_arr)
        merge_sort(right_arr)

        #This is the merging part(conquer) of the code
        i=0 # index of left array
        j=0 # index of right array
        k=0 # index of the merged array

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i +=1

            else:
                arr[k] = right_arr[j]
                j +=1

            k +=1

        # This code is for pushing the remaining elements of left array in the merged array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i +=1
            k +=1

        # This code is for pushing the remaining elemnets of the right array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j +=1
            k +=1

# Driver Code
print("The Array before Sorting is: ",main_arr,"\n")
merge_sort(main_arr)
print("The Array after Sorting is: ",main_arr)





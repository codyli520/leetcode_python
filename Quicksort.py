def quicksort(array):
    if not array:
        return []

    pivot = len(array) - 1 # Picking last element as pivot
    index = 0

    while index < pivot:
        if array[index] > array[pivot]:

            # [8,1,2,3,4]
            # [8,1,2,4,3] 1st swap - pivot and (pivot - 1) to move pivot to the new position
            # [3,1,2,4,8] 2nd swap - index and old pivot position
            array[pivot], array[pivot - 1] = array[pivot - 1], array[pivot]

            if index < pivot - 1:  # to avoid swapping back pivot and (pivot - 1)
                array[index], array[pivot] = array[pivot], array[index]
            pivot -= 1

        else:
            index += 1

        print(array, index, pivot)

        

    left = quicksort(array[:pivot])
    right = quicksort(array[pivot + 1:])

    return left + [array[pivot]] + right


test = [21,4,1,3,9,20,25,6,21,14]
print(quicksort(test))
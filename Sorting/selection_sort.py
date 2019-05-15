# Author:   @Travis-Owens
# Date:     2019-2-4
# Purpose:  Demonstrate how to sort a list using the bubble sort method.

# Video-Reference: https://www.youtube.com/watch?v=g-PGLbMth_g

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr

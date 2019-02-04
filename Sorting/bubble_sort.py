# Author:   @Travis-Owens
# Date:     2019-2-4
# Purpose:  Demonstrate how to sort a list using the bubble sort method.

# Video-Reference: https://www.youtube.com/watch?v=xli_FI7CuzA

def bubbleSort(myList):
    n = len(myList)     # Get length of myList
    for i in range(n):  # Traverse through all array elements
        for j in range(0, n-i-1):   # Last i elements are already in place
            # traverse the array from 0 to n-i-1
            # If myList[j] is greater than myList[j+1] then swap places
            if myList[j] > myList[j+1] :
                temp = myList[j]            # Create a temp variable to hold myList[j]
                myList[j] = myList[j+1]     # Set myList[j] equal to myList[j+1]
                myList[j+1] = temp          # Set myList[j+1] equal to temp
    return myList   # Return sorted list

unsorted_List = [5,2,8,1,7,3,9,4,6]             # A list of un-sorted integers
print("Before Bubble Sort: ", unsorted_List)    # Print unsorted_List, before doing bubble sort
unsorted_List = bubbleSort(unsorted_List)       # Call function bubbleSort and pass the unsorted_list
print("After Bubble Sort: ", unsorted_List)     # Print unsorted_List, which is now sorted

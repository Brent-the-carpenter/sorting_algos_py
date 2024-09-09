# Complete the insertion_sort function according to the given pseudocode:

# For each index in the input list:
# Set a j variable to the current index
# While j is greater than 0 and the element at index j-1 is greater than the element at index j:
# Swap the elements at indices j and j-1
# Decrement j by 1
# Return the list


def insertion_sort(nums):
    for num in range(len(nums)):
        j = num
        while j > 0 and nums[j-1] >= nums[j] :
            nums[j] , nums[j-1] = nums[j-1] , nums[j]
            j -=1 
    return nums 

#O(n^2)
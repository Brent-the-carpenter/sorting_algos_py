
# steps:
# 1. Set swapping to True
# 2. Set end to the length of the input list
#   3.While swapping is True:
#       1.Set swapping to False
#       2.For i from the 2nd element to end:
#           If the (i-1)th element of the input list is greater than the ith element:
#               1.Swap the (i-1)th element and the ith element
#               2.Set swapping to True
#       3.Decrement end by one
#   4.Return the sorted list


def bubble_sort(nums):
    swapping = True
    end = len(nums)-1
    while swapping:
        swapping = False
        for i in range(0 , end):
            if nums[i +1] < nums[i]:
                nums[i+1], nums[i] = nums[i] , nums[i+1]
                swapping = True
        end -=1
    return nums

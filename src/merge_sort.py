
# merge_sort() pseudocode
# Input: A, an unsorted list of integers

# If the length of A is less than 2, it's already sorted so return it
# Split the input array into two halves down the middle
# Call merge_sort() twice, once on each half
# Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
# merge() pseudocode
# Inputs: A and B. Two sorted lists of integers

# Create a new final list of integers.
# Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
# Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
# After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.
# Return the final list.


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    left = merge_sort(nums[:(len(nums)//2)])
    right = merge_sort(nums[(len(nums)//2 ):])
    return merge(left , right)
    
def merge(a, b):
    final_list = []
    i = 0
    j = 0
    while len(a) >i and len(b)>j:
        if a[i] <= b[j]:
            final_list.append(a[i])
            i +=1
        else:
            final_list.append(b[j])
            j +=1
    if i < len(a):
        final_list.extend(a[i:])
    if j < len(b):
        final_list.extend(b[j:])
    return final_list
            
# O(n*log(n))
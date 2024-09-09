
# quick_sort(nums, low, high):
    # If low is less than high:
        # Partition the input list using the partition function
        # Recursively call quick_sort on the left side of the partition
        # Recursively call quick_sort on the right side of the partition
    
    
# partition(nums, low, high):
    # Set pivot to the element at index high
    # Set i to low
    # For each index (j) from low to high
        # If the element at index j is less than the pivot:
            # Increment i by 1
            # Swap the element at index i with the element at index j
    # Swap the element at index i with the element at index high
    # Return the index i


def quick_sort(nums,low , high):
    if low < high:
        pivot = partition(nums , low , high)
        quick_sort(nums , low , pivot-1)
        quick_sort(nums , pivot+1 , high)
        return nums  

def partition (nums, low , high):
    pivot_value = nums[high]
    i = low-1
    for j in range(low , high):
        if nums[j] < pivot_value:
            i +=1
            nums[i], nums[j] = nums[j] , nums[i]
          
    nums[i+1], nums[high] = nums[high] , nums[i+1]
    return i+1


#O(n*log(n)) in average case 
# in absolute worst case O(n^2)
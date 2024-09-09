# For each index:
    # Set smallest_idx to the current index
    # For each index from smallest_idx+1 to the end of the list:
        # If the number at the inner index is smaller than the number at smallest_idx, set smallest_idx to the inner index
    # Swap the number at the current index with the number at smallest_idx


def selection_sort(nums):
    for index in range(len(nums)):
        smallest_index = index
        for i in range(smallest_index+1 , len(nums)):
            if nums[i] < nums[smallest_index]:
                smallest_index = nums[i]
            nums[index], nums[smallest_index] = nums[smallest_index] , nums[index]
    return nums

# O(n^2)
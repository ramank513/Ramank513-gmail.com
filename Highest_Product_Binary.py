def highest_product_of_three(nums):
    if len(nums) < 3:
        raise ValueError("Array must contain at least three integers.")

    nums.sort()

    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

def highest_product_of_three(nums):
    if len(nums) < 3:
        raise ValueError("Need at least three integers")

    nums.sort()
    product1 = nums[-1] * nums[-2] * nums[-3]
    product2 = nums[0] * nums[1] * nums[-1]

    return max(product1, product2)

arr = [10, 10, 1, 3, 2]
print("Highest product of three:", highest_product_of_three(arr))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 3, 4, 5]
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)

        for i in range(1, len(nums)):
            left_products[i] = left_products[i - 1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i+1]

        print(left_products)
        print(right_products)


        return [left_products[i]*right_products[i] for i in range(len(nums))]
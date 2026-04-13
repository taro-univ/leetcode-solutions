class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        #左側積
        left_product = 1
        for i in range(length):
            output[i] = left_product
            left_product *= nums[i] # 後入れすることで"自分より左"を反映

        #右側積を計算しながらoutputに掛け合わせる
        right_product = 1
        for i in range(length-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
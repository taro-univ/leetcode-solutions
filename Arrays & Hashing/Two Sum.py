class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #空のリストを作る
        prevMap = {} #値 : index

        for i, num in enumerate(nums):
            diff = target - num

            #prevMapからインデックスを探す
            if diff in prevMap:
                return [prevMap[diff], i]

            #無かったら格納する
            prevMap[num] = i
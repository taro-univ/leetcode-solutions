class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        stack = []
        next_greater_map = {} #答え格納用のリスト
        answer = [-1] * n1

        for curr_num in nums2:
            while stack and stack[-1] < curr_num:
                prev_num = stack.pop()
                next_greater_map[prev_num] = curr_num
            stack.append(curr_num)

        for i, n in enumerate(nums1):
            answer[i] = next_greater_map.get(n, -1)

        return answer
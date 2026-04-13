class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        res = sorted(count.keys(), key = lambda n: count[n], reverse = True)
        #lambda 引数 : 返り値

        return res[:k]
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #low = 1, high = max(piles)で二分探索
        #while low <= highで k = low + ((high - low) // 2)を試す

        low, high = 1, max(piles)
        count = 0
        while low <= high:
            count = 0
            k = low + ((high - low) // 2)
            for banana in piles:
                count += (banana + k - 1) // k

            if count > h:
                low = k + 1
            elif count <= h:
                high = k - 1

        return low
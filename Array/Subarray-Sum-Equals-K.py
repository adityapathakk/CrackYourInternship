class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, prefSum, d = 0, 0, {0: 1}

        for num in nums:
            prefSum += num
            if prefSum - k in d: res += d[prefSum - k]
            if prefSum not in d: d[prefSum] = 1
            else: d[prefSum] += 1

        print(d)
        return res
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = i
            else:
                return True
        return False
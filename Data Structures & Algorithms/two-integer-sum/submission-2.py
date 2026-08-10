class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        numHash = defaultdict(int)

        for i, n in enumerate(nums):
            diff = target-n
            if diff in numHash and numHash[diff] != i:
                return sorted([i, numHash[diff]])
            numHash[n]=i


        return []
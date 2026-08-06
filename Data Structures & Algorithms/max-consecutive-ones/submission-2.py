class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        collectMax = 0

        val=0
        for i in range(0, len(nums)):
            if nums[i]==1:
                val=val+1
            else:
                collectMax = max(collectMax, val)
                val=0
        collectMax = max(collectMax, val)
        return collectMax




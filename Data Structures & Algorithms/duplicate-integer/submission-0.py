class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a dictionary (hash map) with the number in the list as the first element
        # have the second element that is mapped be the number of times that value is seen, if it is >1, immediately return true
        hashSet = set(nums)
        if len(nums) > len(hashSet):
            return True
        elif len(nums) == len(hashSet):
            return False
        else:
            raise(ValueError)
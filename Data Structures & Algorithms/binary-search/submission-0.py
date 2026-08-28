class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Approach with pointers from both ends
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            # Get the middle pointer (integer division to account for even number list)
            mid = (hi + lo) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                # This means target is greater, so we cut all of the values that are smaller than mid
                lo = mid + 1

            elif nums[mid] > target:
                # Target is smaller, so we cut all values larger than mid
                hi = mid - 1

        return -1
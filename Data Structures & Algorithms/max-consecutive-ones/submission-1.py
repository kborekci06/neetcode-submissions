class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        collect = []

        val=0
        for i in range(0, len(nums)):
            if nums[i]==1:
                val=val+1
            else:
                collect.append(val)
                val=0
        collect.append(val)
        return(max(collect))




        # zeroIndices=[]
        # vals=[]
        # for i in range(0, len(nums)):
        #     if nums[i] == 0:
        #         zeroIndices.append(i)
    
        # if len(zeroIndices) == 0:
        #     return(len(nums))
        # if len(zeroIndices) == 1:
        #     left_sum=len(nums[:zeroIndices[0]])
        #     right_sum=len(nums[zeroIndices[0]:])-1
        #     vals=[left_sum, right_sum]
        #     return(max(vals))
        # if len(zeroIndices) > 1:
        #     for j in range(0, len(zeroIndices)):
        #         if zeroIndices[j]==0:
        #             vals.append(len(nums[:zeroIndices[j]]))
        #         if zeroIndices[j]==(len(nums)-1):
        #             vals.append(len(nums[zeroIndices[j]:]))
        #         else:
        #             vals.append(len(nums[zeroIndices[j-1]:zeroIndices[j]])-1)
        #     return(max(vals))
                


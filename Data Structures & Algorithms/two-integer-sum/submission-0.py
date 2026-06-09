class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(1,len(nums)):
        #         if (nums[i]+nums[j])==target:
        #             return [i,j]
        seen={}
        for i in range(0,len(nums)):
            complement=target-nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]]=i
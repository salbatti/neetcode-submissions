class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        prev=nums[0]
        new=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            tmp=new
            new=max(prev+nums[i],new)
            prev=tmp

        return new
        
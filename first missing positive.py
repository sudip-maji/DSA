class Solution:
    def firstMissingPositive(self, nums) -> int:
#         here we are creating a identity array which tells us the visited numbers and when any number is renmin positive we return the index +1 of that number
        for index in range(len(nums)):
            if nums[index]<=0 or nums[index]>len(nums):
                nums[index]=len(nums)+1
        for num in nums:
            num=abs(num)
            if num<=len(nums) and nums[num-1]>=0:
                nums[num-1]*=-1
        for index in range(len(nums)):
            if nums[index]>0:
                return index+1
        return len(nums)+1
            
#         bruteforce
        # for x in range(1,len(nums)+2):
        #     if x not in nums:
        #         return x

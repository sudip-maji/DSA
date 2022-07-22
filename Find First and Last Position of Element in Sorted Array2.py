class Solution:
    def searchRange(self, nums, target: int) :
        left=self.binarysearch(nums,target,True)
        right=self.binarysearch(nums,target,False)
        return [left,right]
    def binarysearch(self,nums,target,leftbias):
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                i=m
                if leftbias:
                    r=m-1
                else:
                    l=m+1
            
            
        return i
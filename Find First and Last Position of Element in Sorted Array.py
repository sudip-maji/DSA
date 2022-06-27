def searchRange( nums, target) :
        ans=[]
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    ans.append(i)
            j=len(nums)-1
            while j>0:
                if nums[j]==target:
                    ans.append(j)
                else:
                    j-=1
            return ans        
                    
        else:
            return [-1,-1]  
print(searchRange([5,7,7,8,8,10],8))
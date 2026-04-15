class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        
        i = 0 
        #intially I kept i to zero moving if i=j will do nothing but i!=j chanhe j to i and move forward I
        
        
        for j in range(1, len(nums)):
            
            if nums[j] != nums[i]:
                i += 1          
                nums[i] = nums[j] 
        
        
        return i + 1 #last mai I+1 Return Krdia
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr=1
        for i in range (1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[ptr]=nums[i]
                ptr+=1
        return ptr
                
                



        


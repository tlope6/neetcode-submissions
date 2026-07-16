class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = 0
        for i in range(len(nums)) : 
            if nums[i] == i :
                duplicate += 1

        if duplicate == 0 : 
            return False
        else : 
            return True

     

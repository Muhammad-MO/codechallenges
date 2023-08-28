from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
     zero_index = 0
     n = len(nums)
     
     for non_zero_index in range(0,n):
         if(nums[non_zero_index]!=0):
             nums[zero_index] =  nums[non_zero_index]
             zero_index+=1
     for i in range (zero_index,n):
        nums[i] = 0
        print(nums)
             
s = Solution() 
s.moveZeroes([0,2,0,1,4])       
        
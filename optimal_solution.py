from typing import List

class Solution:
    def jump(self, nums):
        jumps, currentEnd, farthest = 0, 0, 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
        return jumps
            
nums = [10,9,8,7,6,5,14,3,2,1,1,1,1,1,1,1,0]
solution = Solution()
result = solution.jump(nums)
print("Result : ", result)   

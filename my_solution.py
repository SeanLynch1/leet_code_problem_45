from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        global_pointer = 0
        total_jumps = 0
        
        if len(nums) == 1:
            return total_jumps
        
        for tanks in nums:
            vision = nums[global_pointer]
            temp_pointer = vision
            
            largest_tank = vision
            
            if vision + global_pointer >= len(nums) - 1:
                total_jumps += 1
                break
            
            # look ahead
            for fuel in range(1, vision + 1):
                if nums[global_pointer + fuel] + fuel >= largest_tank:
                    largest_tank = nums[global_pointer + fuel] + fuel
                    temp_pointer = fuel
            
            global_pointer += temp_pointer
            
            total_jumps += 1
        
        return total_jumps

nums = [10,9,8,7,6,5,14,3,2,1,1,1,1,1,1,1,0]
solution = Solution()
result = solution.jump(nums)
print("Result : ", result)   
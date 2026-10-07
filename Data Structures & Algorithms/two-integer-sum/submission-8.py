class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i, vali in enumerate(nums):
            indices[vali] = i

        for j, valj in enumerate(nums):
            diff = target - valj
            
            if diff in indices and indices[diff] != j:
                return [j, indices[diff]]
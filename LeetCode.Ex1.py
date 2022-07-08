class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = [0,0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(((nums[i] + nums[j]) == target) and i != j ):
                    list[0] = i
                    list[1] = j
        return list
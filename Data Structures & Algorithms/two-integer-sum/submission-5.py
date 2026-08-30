class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = set(nums)
        for i in range (len(nums)):
            a = target - nums[i] 
            if a in myset  :
                for j in range(i+1,len(nums)):
                    if nums[j] == a:
                           
                        return [min(j,i),max(j,i)]
            
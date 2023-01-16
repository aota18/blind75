# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDiff=[]
        # 2 7 11 15  | 9

        for num in nums:
            numDiff.append(num-target)
        
        for i in range(len(nums)):
            for j in range(len(numDiff)):
                if i!=j and nums[i]+numDiff[j]==0:
                    return [i, j]
        
        return []


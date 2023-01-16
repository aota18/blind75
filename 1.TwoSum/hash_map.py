# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # [2, 7, 11, 15]
        # -7: 0
        # -2: 1
        # 2: 2
        # 6: 3
        m={}
        for i in range(len(nums)):
            m[nums[i]-target]=i
        
        print(m)
        for i in range(len(nums)):
            if -nums[i] in m and i!=m[-nums[i]]:
                return [i, m[-nums[i]]]

        
        return []
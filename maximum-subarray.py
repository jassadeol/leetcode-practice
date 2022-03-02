class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float('inf')
        subSum = 0
        start, end = 0, 0
        for i, n  in enumerate(nums):
            subSum += n
            if (subSum > maxSum):
                end = i 
            maxSum = max(maxSum, subSum)
            
            if (subSum < 0):
                subSum = 0
                start = i+1               
            
        return maxSum

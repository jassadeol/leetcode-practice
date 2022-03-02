class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = [height[0]], [-1]*(len(height))
        for l in range(len(height)-1):
            left.append(max(height[l+1], left[l]))
        
        right[-1] = height[-1]
        for r in range(len(height) - 2, -1, -1):
            right[r] = (max(height[r], right[r+1]))
        
        trap = 0
        for i in range(len(height)):
            trap+= min(left[i], right[i]) - height[i]
                       
        return trap

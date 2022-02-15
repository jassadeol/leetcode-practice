#return max amount of water a container can store
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0 
        l = 0
        h = len(height) - 1
        
        #
        while (l <= h):
            a, b = height[l], height[h]
            area = max(area, (h-l)*min(a, b))
            if (a > b):
                h = h - 1
            else:
                l = l + 1
        return area
            
        

                

            

    
            

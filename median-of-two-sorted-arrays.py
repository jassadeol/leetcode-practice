#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1, ptr2 = 0, 0 
        mid = [0, 0]
        totallength = len(nums1) + len(nums2)
        median, prevMedian = 0, 0
        newarr = []
        
        mid[1] = int(((totallength)/2))
        
        #case 0: both arrays
        while (ptr1+ptr2 <= mid[1]) and (ptr1 < len(nums1) and ptr2 < len(nums2)):
            if (nums1[ptr1] <= nums2[ptr2]):
                newarr.append(nums1[ptr1])
                median = nums1[ptr1]
                ptr1 += 1
                if ptr1: prevMedian = nums1[ptr1-1] 
                
            else: 
                newarr.append(nums2[ptr2])
                median = nums2[ptr2]
                ptr2 += 1
                if ptr2: prevMedian = nums2[ptr2-1] 
                
        #case 1: array nums1 and nums2 end reached
        while (ptr1+ptr2 <= mid[1]) and ptr1 < len(nums1):
            newarr.append(nums1[ptr1])
            median = nums1[ptr1]
            ptr1 += 1
            if ptr1: prevMedian = nums1[ptr1-1] 
             
        #case 2: reach end of nums1 and array nums2
        while (ptr1+ptr2 <= mid[1]) and ptr2 < len(nums2):
            newarr.append(nums2[ptr2])
            median = nums2[ptr2]
            ptr2 += 1
            if ptr2: prevMedian = nums2[ptr2-1] 
            
        #print("these are vars")
        #print(median)
        #print(prevMedian)
        if totallength % 2 != 0:
            mid[0] = ceil(totallength-1)/2
            return newarr[int(mid[0])]
        else:
            #mid[0] = int(((totallength)/2)-1)
            return (newarr[mid[1]-1] + newarr[mid[1]])/2
       
       

            
        
        
            
        

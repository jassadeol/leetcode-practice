class Solution {
    public int removeDuplicates(int[] nums) {
        int ptr = 1; 
        if (nums.length > 1)
    {
            for (int i= 1; i < nums.length ; i++)
        {
            
           if (nums[ptr - 1] != nums[i])
           {
               nums[ptr++] = nums[i];
               //search = nums[i+1];
           }
        }
            return ptr;
    }
        else
        {
            return nums.length;
        }        
    }
}

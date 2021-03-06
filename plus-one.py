class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + carry
            if (digits[i] > 9):
                digits[i] = 0
                carry = 1
            else:
                carry = 0
            
        return digits if carry == 0 else [1] + digits

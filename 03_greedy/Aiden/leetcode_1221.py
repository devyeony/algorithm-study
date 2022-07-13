class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = right = result = 0
        
        for c in s:
            if c == 'L':
                left +=1
            else:
                right +=1
                
            if left == right:
                left = right = 0
                result +=1
        
        return result
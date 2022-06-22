class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        return lst == lst[::-1]
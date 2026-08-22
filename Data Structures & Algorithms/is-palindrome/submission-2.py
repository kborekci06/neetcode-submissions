class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return False
        
        left = 0
        right = len(s)-1
    
    
        while left < right:

            while left < right and s[left].isalnum() == False:
                # Incr to next index
                left += 1
            while left < right and s[right].isalnum() == False:
                # Incr to next index
                right -= 1
    
            s_left = s[left].lower()
            s_right = s[right].lower()
    
            if s_left == s_right:
                left += 1
                right -= 1
            else:
                print(s_left)
                print(s_right)
                return False
            
        return True

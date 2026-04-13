class Solution:
    def isPalindrome(self, s: str) -> bool:
        #at first, made two pointers
        i = 0
        j = len(s) - 1

        while i < j:

            #detection of Alphanumeric Character
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            #convert to lowercase
            low_s_left = s[i].lower()
            low_s_right = s[j].lower()

            #isPalindrome
            if low_s_left != low_s_right:
                return False

            i += 1
            j -= 1
        
        return True
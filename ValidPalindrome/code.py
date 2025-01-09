
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for ch in s:
            if ch.isalnum():
                new_str += ch

        return new_str.lower() == (new_str[::-1]).lower()



import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "").strip()
        punc = string.punctuation
        
        for ch in s:
            if ch in punc:
               s = s.replace(ch,"")
               

        str1 = ''
        for i in range(len(s)-1, -1, -1):
            str1 += s[i]
        return str1.lower() == s.lower()
        
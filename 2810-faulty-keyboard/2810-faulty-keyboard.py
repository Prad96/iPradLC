class Solution:
    def finalString(self, s: str) -> str:
        final_string=''
        for i in s:
            if i != 'i':
               final_string+=i
            else:
               final_string=final_string[::-1]
        return final_string
          
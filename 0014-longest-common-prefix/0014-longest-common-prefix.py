class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        if len(strs)==0:
            return ''
        elif len(strs)==1:
            return strs[0]
        longestPrefix=''
        first_string=strs[0]
        last_string=strs[-1]
        for string in range(len(first_string)):
            if first_string[string]!=last_string[string]:
                break
            longestPrefix+=first_string[string]
        return longestPrefix
            
        
            
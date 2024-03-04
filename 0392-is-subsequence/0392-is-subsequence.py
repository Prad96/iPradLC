class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s_list=list(s)
        # t_list=list(t)
        # flag=1
        # for i in range(len(s_list)):
        #   if s_list[i] not in t_list:
        #       flag=0
        #       break
        # if flag==0:
        #   return False
        # return True
        pointer_one=pointer_two=0
        while pointer_one<len(s) and pointer_two<len(t):
            if s[pointer_one]==t[pointer_two]:
                pointer_one+=1    
            pointer_two+=1
        if pointer_one==len(s):
           return True
        return False
            
        
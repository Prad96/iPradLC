import math
class Solution:
    def isHappy(self, n: int) -> bool:
        number_list=[]
        number_list.append(n)
        while n!=1:
          digit_sum=0
          for i in str(n):
              digit_sum+=int(i)**2
          if digit_sum not in number_list:
                 number_list.append(digit_sum)
          else:
                 return False
          n=digit_sum
        return True
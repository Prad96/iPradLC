class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
      
        tokens=sorted(tokens)
        score=0
        max_score=0
        left=0
        right=len(tokens)-1
        
        while left<=right:
          
          if power>=tokens[left]:
             power-=tokens[left]
             left+=1
             score+=1
             max_score=max(max_score,score)
             
          elif score>0:
               power+=tokens[right]
               right-=1
               score-=1
          else:
              break
        return max_score
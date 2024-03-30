class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorsCount=0
        for detail in details:
            if int(detail[-4:-2])>60:
                seniorsCount+=1
        return seniorsCount
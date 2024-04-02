class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=list()
        for height,name in sorted(zip(heights,names),reverse=True):
            people.append(name)
        return people
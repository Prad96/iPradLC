class Solution:
    def capitalizeTitle(self, title: str) -> str:
        capitalized=[]
        titles=title.split()
        
        for t in titles:
            if len(t)>2:
                capitalized.append(t.capitalize())
            else:
                capitalized.append(t.lower())
        return ' '.join(capitalized)
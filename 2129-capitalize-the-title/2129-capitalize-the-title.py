class Solution:
    def capitalizeTitle(self, title: str) -> str:
        capitalized=[]
        for t in title.split():
            if len(t)>2:
                capitalized.append(t.capitalize())
            else:
                capitalized.append(t.lower())
        return ' '.join(capitalized)
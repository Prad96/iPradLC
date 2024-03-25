class Solution:
    def frequencySort(self, s: str) -> str:
        frequency={}
        frequent,onlyonce='',''
        for char in s:
            frequency[char]=frequency.setdefault(char,0)+1
        print(frequency)
        for key,value in sorted(frequency.items(),key=itemgetter(1),reverse=True):
            # print(key, value)
            if value==1:
                onlyonce+=key
                # print("onlyonce",onlyonce)
            else:
                # print('multime',frequent)
                frequent+=(key)*value
        return frequent+onlyonce
                
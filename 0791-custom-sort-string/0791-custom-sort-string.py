class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output_string=''
        for i in order:
            for k in range(s.count(i)):
                output_string+=i
                # print(output_string)
        for j in s:
            if j not in order:
                output_string+=j
                # print(output_string)
        return output_string
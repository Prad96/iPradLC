class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbol_value={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        integer_value=0
        for symbol in range(len(s)):
            if symbol+1 < len(s)  and roman_symbol_value[s[symbol]] <roman_symbol_value[s[symbol+1]]:
                integer_value-=roman_symbol_value[s[symbol]]
            else:
                integer_value+=roman_symbol_value[s[symbol]]
        return integer_value
    
    
    
        
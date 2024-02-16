class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mul3= mul5 = 0
        fizzbuzz_list = []   
        for i in range(1, n + 1):
            ch = ''
            mul3 += 1
            mul5 += 1
            
            if mul3 == 3:
                ch += 'Fizz'
                mul3 = 0
            
            if mul5 == 5:
                ch += 'Buzz'
                mul5 = 0
            
            if not ch:
                fizzbuzz_list.append(str(i))
            else:
                fizzbuzz_list.append(ch)
        
        return fizzbuzz_list
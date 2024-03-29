class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelCount=0
        for stone in stones:
            if stone in jewels:
                jewelCount+=1
        return jewelCount
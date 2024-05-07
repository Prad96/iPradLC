class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keys={' ':' '}
        decoded_message=''
        alphabets='abcdefghijklmnopqrstuvwxyz'
        alphabet=0
        for char in key:
            if char not in keys:
                keys[char]=alphabets[alphabet]
                alphabet+=1
        for char in message:
            decoded_message+=keys[char]
        return decoded_message
            
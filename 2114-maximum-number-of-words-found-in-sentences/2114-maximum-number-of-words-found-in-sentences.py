class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mostWords=0
        for sentence in sentences:
            sen=sentence.split()
            sen_len=len(sen)
            mostWords=max(sen_len,mostWords)
        return mostWords
        
        
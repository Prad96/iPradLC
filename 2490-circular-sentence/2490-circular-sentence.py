class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        circular=True
        if len(sentence)==1 and sentence[0]!=sentence[-1]:
            return not circular
        sentences=sentence.split()
        for word in range(len(sentences)):
            if sentences[word][-1]!=sentences[(word+1)%len(sentences)][0]:
                return not circular
        return circular
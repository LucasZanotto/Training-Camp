class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wordMerge = ""
        counter = 0

        if len(word1) >= len(word2):
            counter = len(word1)
        else:
            counter = len(word2)
        
        for i in range(counter):
            if len(word1) - 1 < i:
                wordMerge += word2[i]
            elif len(word2) - 1 < i:
                wordMerge += word1[i]
            else:
                wordMerge += word1[i]
                wordMerge += word2[i]
            
        return wordMerge
    
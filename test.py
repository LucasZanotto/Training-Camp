class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vowelsList = []
        vowelsInverted = ''
        for i in s:
            if vowels.__contains__(i):
                vowelsList.append(i)

        for j in s: 
            if vowels.__contains__(j):
                vowelsInverted += vowelsList[-1]
                vowelsList.pop()
                continue
            vowelsInverted += j
        return vowelsInverted

#find index containing letter

class Solution:
    def findWordsContaining(self, words, x):
        array = []
        for i,  word in enumerate(words):
            if x in word:
                array.append(i)
        return array
    
    #one liner solution:
        #return [i for i in range(len(words)) if x in words[i]]

s = Solution()
words = ["leet","code"]
x = "e"
print(s.findWordsContaining(words, x))

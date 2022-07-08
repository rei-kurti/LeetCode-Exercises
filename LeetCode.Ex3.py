class Solution:
    def lengthOfLongestSubstring(self, s:str)->int:
        word = list(s)
        if len(word) != 0:
            answer = 1
            longest = word[0]
            new = 0
            for i in range (1,len(word)):
                unique = True
                for j in range (new,i):    
                    if word[i] == word[j]:
                        unique = False                        
                        longest = word[j+1]
                        new = j+1
                        for k in range(j+1,i+1):
                            if word[k]!=word[j+1]:
                                longest += word[k]
                        break
                if unique == True:
                    longest = longest + word[i]
                if len(longest) > answer:
                    answer = len(longest)
            return answer
        else:
            return 0
    
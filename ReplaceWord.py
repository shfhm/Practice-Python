
class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        self.dict=dict
        self.sentence={}
        
        for key in dict:
            temp=key
            for word in sentence.split():
                if word.find(temp) == 0:
                    sentence=sentence.replace(word, key, 1)   
        return sentence
    
    
dict = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
s=Solution()
print(s.replaceWords(dict,sentence))


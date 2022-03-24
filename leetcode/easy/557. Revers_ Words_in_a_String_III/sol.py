class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ''
        for word in s.split(' '):
            print(word)
            answer += ''.join(reversed(word)) + ' '
        
        return answer.rstrip()
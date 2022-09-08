# Easy
'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

'''

# Solution 1: Stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(l):
            res = []
            for i in l:
                if i != '#':
                    res.append(i)
                elif res:
                    res.pop()
            return res

        return build(s) == build(t)
        
# Solution 2:
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, t1 = len(s)-1, len(t)-1
        skip1, skip2 = 0,0
        while s1 >=0 or t1>=0:
            while s1 >=0:
                if s[s1] =='#':
                    s1 -=1
                    skip1 +=1
                elif skip1 >0:
                    s1 -=1
                    skip1 -=1
                else:
                    break

            while t1 >=0:
                if t[t1] =='#':
                    t1 -=1
                    skip2 +=1
                elif skip2 >0:
                    t1 -=1
                    skip2 -=1
                else:
                    break
            if t1>=0 and s1>=0:
                if s[s1] != t[t1]:
                    return False 
            elif t1 >=0 or s1>=0:
                return False
            s1-=1
            t1-=1

        return True

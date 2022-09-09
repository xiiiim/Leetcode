# Medium

'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''
# Two Pointers with Sliding Window

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_1 = {}
        hash_2 = collections.Counter(p)
        k = len(p)
        res = []
        start = 0
        for end in range(len(s)):
            hash_1[s[end]] = hash_1.get(s[end], 0) +1
            print(hash_1)

            if hash_1 == hash_2: # Note character can be repeated so cannot use len()
                res.append(start)
            if end >= k -1:
                hash_1[s[start]] -=1
                if not hash_1[s[start]]:
                    del hash_1[s[start]]
                start +=1
        return res

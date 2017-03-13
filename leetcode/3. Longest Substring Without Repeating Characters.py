'''Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.'''




class Solution(object):

    def lengthOfLongestSubstring(self, s):
        cmn_str = ''
        max_len = 0
        for i in s:
            if cmn_str not in s:
                cmn_str = cmn_str + i
                print cmn_str
            else:
                tmp = len(cmn_str)
                if tmp > max_len:
                    max_len = tmp




        return max_len

a = Solution()
print a.lengthOfLongestSubstring('abcabcabc')



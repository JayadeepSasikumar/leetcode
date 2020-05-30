class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Link to problem:
            https://leetcode.com/problems/longest-substring-without-repeating-characters/

        Problem statement:
            Given a string, find the length of the longest substring
            without repeating characters.

        Example 1:
            Input: "abcabcbb"
            Output: 3 
            Explanation: The answer is "abc", with the length of 3. 

        Example 2:
            Input: "bbbbb"
            Output: 1
            Explanation: The answer is "b", with the length of 1.

        Example 3:
            Input: "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3. 

        Note that the answer must be a substring, "pwke" is a
        subsequence and not a substring.

        Arg -
            s - str

        Pseudocode -
            1. Initialiase two empty strings current_string and
               longest_string
            2. Initialise a flag is_reading. This should be reset when
               a character repeats.
            3. For each char in s:
                i. if char in current_string:
                    - reset is_reading
                    - if length of current string is the greatest:
                      - update longest_string if so
                    - set current_string's position to first index of
                      char + 1
                   else:
                    - append char to current_string
                    - set is_reading
            4. If is_reading is set:
                - if length of current string is the greatest:
                    return len(current_string)
            5. Return len(longest_string)

        Returns -
            result - int, length of longest string.
        """
        current_string = ""
        longest_string = ""
        is_reading = True
        for char in s:
            if char in current_string:
                is_reading = False
                if len(current_string) > len(longest_string):
                    longest_string = current_string
                current_string = current_string[current_string.index(
                    char) + 1:] + char
            else:
                is_reading = True
                current_string += char
        if is_reading:
            if len(current_string) > len(longest_string):
                return len(current_string)
        return len(longest_string)

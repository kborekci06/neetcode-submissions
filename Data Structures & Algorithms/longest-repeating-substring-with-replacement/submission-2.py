class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        # dictionary to record the state - running frequency count of the contents of the window
        freqDict = defaultdict(int)
        maxLen = 0
        L = 0

        for R, ch in enumerate(s):

            # Record the frequency of the char
            freqDict[ch] += 1

            # While the condition that satisfies a window is still not met
            while (R-L+1) - max(freqDict.values()) > k:
                # Decrement the character's window count
                freqDict[s[L]] -= 1
                # Shrink the window by advancing the L pointer / Walk until the window condition is satisfied
                L += 1

            # Record the maximum length of the current window
            maxLen = max(maxLen, (R-L+1))

        return maxLen

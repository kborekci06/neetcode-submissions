class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Window state - shrink or grow based on conditions
        state = set()
        # Max window
        maxW = 0
        # Pointers
        R=0
        L = 0

        while R < len(s):

            # print("right", s[R])

            # remove the repeated elements if the new candidate element is already in there
            while s[R] in state:
                # print(s[L], "left")
                state.remove(s[L])
                # print(state, "SET")
                L +=1

            state.add(s[R])
            # print(state, "FINAL SET")

            # Record max window size of unique elements
            maxW = max(maxW, len(state))

            R+=1
        return maxW
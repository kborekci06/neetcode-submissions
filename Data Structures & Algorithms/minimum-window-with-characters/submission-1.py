class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Removes the inefficiency from O(26) search when using all()
        '''
        from collections import Counter


        # The count we need
        need = Counter(t)

        # The count we have currently
        have = Counter()

        # How many distinct characters in need satisfy have[c] >= need [c]
        formed = 0

        L = 0
        best_L = 0
        best_len = float("inf")

        for R, ch in enumerate(s):

            # 1. GROW
            # Add count of what we have
            have[ch] += 1
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # 2. SHRINK
            # Shrink when the window is valid
            # The window is valid when the the count of what we have is >= what we need
            while formed == len(need):
                # 3. RECORD
                # Record the best window
                if (R - L + 1) < best_len:
                    best_L = L
                    best_len = R - L + 1

                if s[L] in need and have[s[L]] == need[s[L]]:
                    formed -= 1

                # Shrink the window
                have[s[L]] -= 1 # Reduce count of what we have in the window

                # Advance the L pointer
                L += 1

        # return <value if true> if <condition> met, else <value if false>
        return s[best_L : best_L + best_len] if best_len != float('inf') else ""
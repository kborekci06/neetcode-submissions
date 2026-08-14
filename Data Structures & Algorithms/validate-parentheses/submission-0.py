class Solution:
    def isValid(self, s: str) -> bool:
        # Most recently opened bracket must be the first one closed
            # "Most recent first" = LIFO = stack
        
    
        pairs = {")" : "(", "]" : "[", "}" : "{"}

        stackString = []

        s = list(s)

        for ch in s:
            if ch in pairs:
                if not stackString or stackString.pop() != pairs[ch]:
                    return False
            else:
                stackString.append(ch)
        return not stackString # Means if it is an empty stack aka not [] then True
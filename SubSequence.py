class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (s == ""):
            return True
        c = 0
        for i in range(0, len(t)):
            if (c< len(s) and s[c] == t[i]):
                c += 1

        if (c == len(s)):
            return True

        return False


solucion = Solution()

print(solucion.isSubsequence("pro", "perro"))

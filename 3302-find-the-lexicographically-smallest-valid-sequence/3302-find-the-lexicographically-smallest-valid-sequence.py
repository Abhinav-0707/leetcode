class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # suf[j] = index in word1 where word2[j:]
        # can start as an exact subsequence.
        suf = [-1] * m

        p = n - 1

        for j in range(m - 1, -1, -1):
            while p >= 0 and word1[p] != word2[j]:
                p -= 1

            if p < 0:
                break

            suf[j] = p
            p -= 1

        ans = []
        i = 0
        used_change = False

        for j in range(m):
            # Try to find the smallest possible index.
            while i < n:
                # Case 1: exact match
                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    break

                # Case 2: use our one allowed change.
                if not used_change:
                    # We need the rest word2[j+1:] to be
                    # exactly matchable after i.
                    if j == m - 1:
                        ans.append(i)
                        i += 1
                        used_change = True
                        break

                    if suf[j + 1] != -1 and suf[j + 1] > i:
                        ans.append(i)
                        i += 1
                        used_change = True
                        break

                i += 1
            else:
                return []

        return ans
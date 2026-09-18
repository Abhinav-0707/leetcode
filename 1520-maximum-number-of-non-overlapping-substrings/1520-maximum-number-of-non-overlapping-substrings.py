class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        n = len(s)

        # Find first and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid substring for each character
        for c in range(26):

            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:

                idx = ord(s[i]) - ord('a')

                # This character appeared before our left boundary
                if first[idx] < left:
                    valid = False
                    break

                # Include all occurrences of this character
                right = max(right, last[idx])

                i += 1

            if valid:
                intervals.append((left, right))

        # Choose intervals that finish earliest
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:

            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result
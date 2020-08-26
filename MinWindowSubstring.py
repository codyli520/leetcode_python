class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        left = 0
        right = 0

        min_window = ""

        target_letter_count = Counter(t)

        target_count = len(t)

        for right in range(len(s)):
            if s[right] in t:
                if target_letter_count[s[right]] > 0:
                    target_count -= 1
                target_letter_count[s[right]] -= 1

            while target_count == 0:
                word = s[left: right + 1]

                if not min_window or len(word) < len(min_window):
                    min_window = word

                if s[left] in t and target_letter_count[s[left]] <= 0:
                    target_letter_count[s[left]] += 1
                    if target_letter_count[s[left]] > 0:
                        target_count += 1

                left += 1

        return min_window













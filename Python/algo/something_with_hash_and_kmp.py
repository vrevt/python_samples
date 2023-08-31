class Solution:

    # https://leetcode.com/problems/shortest-palindrome/solutions/60153/8-line-o-n-method-using-rabin-karp-rolling-hash/
    # There is a slight chance that ther could be a hash collision. But this is very
    # unlikely. And we can add check for this where we save all the i values when
    # hash was equal and then compare the i values to see if the sbstring is a palandrome
    def usingRK(self, s):
        # Convert letter to id
        def id(letter):
            return ord(letter) - ord('a')

        hash1, hash2 = 0, 0
        base = 26
        mod = 10 ** 9 + 7
        power = 1  # We update power so new incoming letter gets highest weight
        # The first character will be a palandrome. So we no longer palandrome we can atleast
        # use this: abcd --> dcbabcd (we reuse a and only reverse bcd since a is a palandrome)
        pal = 0
        for i in range(len(s)):
            hash1 = (hash1 * base + id(s[i])) % mod  # First char has highest weight
            hash2 = (hash2 + id(s[i]) * power) % mod  # Last char has highest weight
            power = power * base  # Power is updated each time so its equal to base ^ (n-1)
            if hash1 == hash2:
                print(i)
                # For aacecaaa this will be true for 0, 1, 6 index
                # This works because we calculate hash in 2 directions
                # 1st - Leftmost char has highest weight
                # 2nd - Leftmost char has least weight
                # When all the characters in string form palandrome
                # The weights will balance each other and the hash will be same
                pal = i
        # Reverse substring that is not part of palandrome
        reversed_suffix = s[pal + 1:][::-1]
        return reversed_suffix + s

    def usingKMP(self, s):
        def longestSuffixPrefix(s):
            lsp = [0] * len(s)
            for end in range(1, len(s)):
                start = lsp[end - 1]
                while start > 0 and s[start] != s[end]:
                    start = lsp[start - 1]
                if s[start] == s[end]:
                    lsp[end] = start + 1
            return lsp

        # We need # to seperate string and its reverse
        # Consider aaaa
        # s + rev: aaaa|aaaa
        # The LPS value for last a will be 7 for aaaaaaa.
        # But we don't want this. We are only interested in LSP of original string
        # When we add a # the hash will be close to prefix start than suffix start
        # So any thing beyond the length of original string will not be considered
        # [a{aaa#aaa]a} notice how # is closer to 1 than other?
        rev = s[::-1]
        s_and_rev = s + "#" + rev

        # We are calculating the LSP table of KMP.
        lsp = longestSuffixPrefix(s_and_rev)

        # Ref - https://www.youtube.com/watch?v=c4akpqTwE5g
        # Consider abab
        # If we appended its reverese to the start then we would definiely get a palandrome
        # baba|abab
        # But this is not the shortest palandrome. This is because abab has a palandrome in it
        # [aba]b.
        # So we get extra aba in the reverse string we attach.
        # This extra aba is nothing but longest commpon prefix suffix when we attach s and s reversed:
        # [aba]b|b[aba]
        # Now KMPs LSP table for last element will have value 3, since we have aba matching.
        # So if we ignore those characters then we can just append b from reverse to start of abab to
        # get shortest palandrome.
        return rev[0:len(s) - lsp[-1]] + s

    # Will run in O(N)
    def shortestPalindrome(self, s: str) -> str:

        return self.usingRK(s)

        # return self.usingKMP(s)

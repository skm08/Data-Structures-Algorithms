class Solution:
    def isVowel(self, c: str) -> bool:
        return c in {'a', 'e', 'i', 'o', 'u'}

    def findNextConsonant(self, word: str, next_consonant: list) -> None:
        n = len(word)
        next = n
        for i in range(n - 1, -1, -1):
            next_consonant[i] = next
            if not self.isVowel(word[i]):
                next = i

    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        next_consonant = [0] * n
        self.findNextConsonant(word, next_consonant)

        count = 0
        consonants = 0
        vowel_freq = {}
        left = 0
        right = 0
        prev = -1

        while right < n:
            if prev != right:
                if self.isVowel(word[right]):
                    vowel_freq[word[right]] = vowel_freq.get(word[right], 0) + 1
                else:
                    consonants += 1
                prev = right

            if right >= (5 + k - 1):
                if len(vowel_freq) == 5 and consonants == k:
                    count += next_consonant[right] - right

                # Move left ptr to right: Shrink window
                if (len(vowel_freq) == 5 and consonants == k) or (consonants > k):
                    if self.isVowel(word[left]):
                        vowel_freq[word[left]] -= 1
                        if vowel_freq[word[left]] == 0:
                            del vowel_freq[word[left]]
                    else:
                        consonants -= 1
                    left += 1
                else:
                    right += 1
            else:
                right += 1

        return count
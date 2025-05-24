class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i, word in enumerate(words):
            if x in word.lower():
                indices.append(i)
        return indices
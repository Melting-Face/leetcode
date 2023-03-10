class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_length = len(word1)
        word2_length = len(word2)
        double_array = [[0 for i in range(word2_length + 1)] for i in range(word1_length + 1)]
        for i in range(word1_length + 1):
            for j in range(word2_length + 1):
                if i == 0 or j == 0:
                    continue
                if word1[i-1] == word2[j-1]:
                    double_array[i][j] = double_array[i-1][j-1] + 1
                else:
                    double_array[i][j] = max(double_array[i-1][j], double_array[i][j-1])
        
        fix_count = word1_length + word2_length - (2 * double_array[word1_length][word2_length])
        return fix_count

        
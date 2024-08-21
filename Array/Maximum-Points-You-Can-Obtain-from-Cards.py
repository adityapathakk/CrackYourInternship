class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum, rightSum = sum(cardPoints[:k]), 0
        result = leftSum

        for i in range(k):
            leftSum -= cardPoints[k - 1 - i]
            rightSum += cardPoints[len(cardPoints) - 1 - i]
            result = max(result, leftSum + rightSum)

        return result
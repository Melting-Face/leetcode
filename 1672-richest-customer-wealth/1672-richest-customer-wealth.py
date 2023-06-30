class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = None
        for account in accounts:
            if not max_value:
                max_value = sum(account)
            max_value = max(max_value, sum(account))
        return max_value
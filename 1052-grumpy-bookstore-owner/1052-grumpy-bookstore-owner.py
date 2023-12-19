class Solution:
    def maxSatisfied(
        self,
        customers: List[int],
        grumpy: List[int],
        minutes: int,
    ) -> int:
        zipped_customers = zip(customers, grumpy)
        satisfied_customers = sum(
            customers[:minutes] + [c * bool(not g) for i, (c, g) in enumerate(zipped_customers) if i >= minutes],
        )
        max_satisfied_customers = satisfied_customers
        for i in range(0, len(customers) - minutes):
            satisfied_customers -= (customers[i] if grumpy[i] else 0)
            satisfied_customers += customers[i + minutes] if grumpy[i + minutes] else 0
            max_satisfied_customers= max(
                max_satisfied_customers,
                satisfied_customers,
            )
        return max_satisfied_customers

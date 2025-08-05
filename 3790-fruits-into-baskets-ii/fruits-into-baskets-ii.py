from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruit_sizes: List[int], basket_capacities: List[int]) -> int:
        total_fruits = len(fruit_sizes)
        unplaced_fruits = total_fruits

        for fruit in fruit_sizes:  # \U0001f34e Loop through each fruit
            for i in range(len(basket_capacities)):  # \U0001f9fa Try placing in a basket
                if fruit <= basket_capacities[i]:
                    basket_capacities[i] = 0  # \U0001f6ab Mark basket as used
                    unplaced_fruits -= 1     # ✅ Fruit placed
                    break

        return unplaced_fruits  # \U0001f4e6 Total unplaced fruits
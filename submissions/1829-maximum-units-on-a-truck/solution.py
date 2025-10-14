# Defining a problem structure
# truckSize - max amount of boxes & boxTypes = [numberOfBoxesi, numberOfUnitsPerBoxi]
# So, we need to put as much units on the truck as possible. In order to do that, we will count amount of units from box type which we can store in the truck, starting from the most useful box - which is the largest one,  with most units. Return units 


# Edge cases
# Truck size can't contain any box (any box is too large)

# Approach
# 1. Brute force one - sort by the unit key, and iterate thorugh each boxType if boxType boxes number is > 0
# 2. 

# TC and SC

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box_types = sorted(boxTypes, key=lambda sorted_box: sorted_box[1], reverse=True) # O(n * log n)
        units = 0
        boxes_count = 0
        
        for sorted_box in sorted_box_types:
                diff = min(truckSize - boxes_count, sorted_box[0])
                units += diff * sorted_box[1]
                boxes_count += diff
                    
        return units

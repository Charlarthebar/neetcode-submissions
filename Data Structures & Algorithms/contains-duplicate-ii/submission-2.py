class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0
        have = set()

        while j < len(nums):
            if nums[j] in have:
                return True
            if abs(i - j) < k:
                have.add(nums[j])
                j += 1
                continue
            have.add(nums[j])
            have.remove(nums[i])
            i += 1
            j += 1
            # print(have)
            
            
            
            
            
            
            
        
        return False            
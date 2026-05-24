class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        # mid = 2


        while l < r-1:
            mid = (l + r) // 2
            if nums[mid] > nums[r] and nums[l] > nums[r] and nums[mid] > nums[l]:
                # split between mid and r
                l = mid
            elif nums[l] > nums[mid] and nums[l] > nums[r] and nums[mid] < nums[r]:
                # split between l and mid
                r = mid
            elif nums[r] > nums[l] and nums[mid] > nums[l] and nums[r] > nums[mid]:
                return nums[0]
        
        if nums[l] == nums[r]:
            return nums[l]
        return min(nums[l], nums[r])


                
            

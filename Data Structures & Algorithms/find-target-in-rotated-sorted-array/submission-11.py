class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1



        # while l < r:
        #     mid = (l+r) // 2
        #     if nums[mid] >= nums[l]:
        #         l = mid + 1
        #     else:
        #         r = mid 
        # print(r)
        # print(l)
        # if target <= nums[r] and target >= nums[0]: # in left side
        #     l = 0
        #     print("in left")
        # else: 
        #     r = len(nums)-1
        #     print("in right")

        # print(r)
        # print(l)
        # while l <= r:
        #     mid = (l+r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return -1

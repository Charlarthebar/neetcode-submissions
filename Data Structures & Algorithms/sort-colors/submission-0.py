class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergesort(arr, l, r):
            if l >= r:
                return [arr[l]]
            m = (l + r) // 2
            mergesort(arr, l, m), mergesort(arr, m + 1, r)
            arr1, arr2 = arr[l:m+1], arr[m+1:r+1]
            p1, p2 = 0, 0
            i = l
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] <= arr2[p2]:
                    nums[i] = arr1[p1]
                    p1 += 1
                else:
                    nums[i] = arr2[p2]
                    p2 += 1
                i += 1
            while p1 < len(arr1):
                nums[i] = arr1[p1]
                p1 += 1
                i += 1
            while p2 < len(arr2):
                nums[i] = arr2[p2]
                p2 += 1
                i += 1
            return

        mergesort(nums, 0, len(nums) - 1)
        return nums
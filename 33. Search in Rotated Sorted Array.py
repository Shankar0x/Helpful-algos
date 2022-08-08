class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target not in nums:
        #     return -1
        # return nums.index(target)
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=int((low+high)/2)
            if(nums[mid]==target):
                return mid
            #Left half is sorted
            if(nums[low]<nums[mid]):
                if(target>=nums[low] and target<=nums[mid]):
                    high=mid-1
                else:
                    low=mid+1
            elif(nums[high]>nums[mid]):
                if(target>=nums[mid] and target<=nums[high]):
                    low=mid+1
                else:
                    high=mid-1
        return -1

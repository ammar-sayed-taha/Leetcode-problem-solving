class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            n = nums[j]
            cnt = 0

            result +=  int(str(nums[i]) + str(nums[j]))
            i+=1
            j-=1

        if len(nums) % 2 != 0:
            result += nums[i]

        return result
        
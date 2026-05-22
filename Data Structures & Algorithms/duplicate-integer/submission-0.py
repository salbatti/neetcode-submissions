class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets=set()

        for i in nums:
            if i not in sets:
                sets.add(i)

            else:
                return True

        return False
        
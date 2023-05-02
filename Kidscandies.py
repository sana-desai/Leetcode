class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies=max(candies)
        result_lst=[]
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candies:
                result_lst.append(True)
            else:
                result_lst.append(False)
        return result_lst
a=Solution()
list1=[]
list1=(a.kidsWithCandies([2,3,5,1,3],3))
print(list1)
            
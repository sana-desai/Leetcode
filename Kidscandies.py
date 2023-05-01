class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies=max(candies)
        result_lst=[]
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candies:
                result_lst.append(True)
            else:
                result_lst.append(False)
        return result_lst
            
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print (matrix)
        def binarySearch(row):
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                val = row[mid]
                if  val == target:
                    return True
                elif row[mid] > target:
                    r -= 1
                else:
                    l += 1
        
        for row in matrix:
            if binarySearch(row):
                return True
        return False
                
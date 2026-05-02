class Solution:
    def binarySearch(self, arr: list[int], target: int) -> bool:
        N = len(arr)
        left = 0
        right = N - 1

        while left <= right:
            mid = (left + right)//2

            if target ==arr[mid]:
                return True
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        up = 0
        bottom = R - 1

        while up <= bottom:
            mid = (up + bottom)//2

            if target >= matrix[mid][0] and target <= matrix[mid][C-1]:
                #binary search on matrix[mid]
                return self.binarySearch(matrix[mid], target)
            elif target > matrix[mid][C-1]:
                up = mid + 1
            else:
                bottom = mid -1 

        return False
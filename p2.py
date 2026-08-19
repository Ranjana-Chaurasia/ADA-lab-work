#Design a Sort class containing merge_sort(arr: List[int]) -> List[int] and quick_sort(arr: List[int]) -> List[int] methods that accept an unsorted integer array and return the sorted array.
class Sort:

    # Merge Sort
    # Divides the array into halves, recursively sorts them, and merges them.
    # Time Complexity: O(n log n)
    def merge_sort(self, arr: list[int]) -> list[int]:

        if len(arr) <= 1:
            return arr
        
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        result = []

        i=0
        j=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # Quick Sort
    # Selects a pivot, partitions elements around it, and recursively sorts them.
    # Average Time Complexity: O(n log n)
    # Worst-case Time Complexity: O(n²)
    def quick_sort(self, arr: list[int]) -> list[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        smaller = []
        equal = []
        larger = []

        for num in arr[:-1]:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                larger.append(num)
            else:
                equal.append(num)
        equal.append(pivot)

        smaller = self.quick_sort(smaller)
        larger = self.quick_sort(larger)

        return smaller + equal + larger

# Test cases
s = Sort()
arr = [8, 3, 5, 2, 7, 8, 1, 4]
print(s.merge_sort(arr))
print(s.quick_sort(arr))
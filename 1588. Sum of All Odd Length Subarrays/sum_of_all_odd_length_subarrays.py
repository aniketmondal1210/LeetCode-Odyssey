class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        a = get_all_subarrays(arr)
        result = 0
        for i in a:
            if len(i) % 2 != 0:
                result += sum(i)
        return result


def get_all_subarrays(array):
    n = len(array)
    subarrays = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarrays.append(array[i:j])
    return subarrays

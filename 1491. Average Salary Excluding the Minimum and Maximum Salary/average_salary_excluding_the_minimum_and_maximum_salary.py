class Solution:
    def average(self, salary: List[int]) -> float:
        new_list = salary
        new_list.remove(min(salary))
        new_list.remove(max(salary))
        return sum(new_list)/len(new_list)

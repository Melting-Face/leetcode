class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        tuple_list_of_values = [ (index, num) for index, num in enumerate(nums) ]
        for start_index, first_value in enumerate(tuple_list_of_values): 
            first_index, first_num = first_value
            some_values = tuple_list_of_values[first_index:]
            for second_value in some_values:
                second_index, second_num = second_value
                if target == first_num + second_num and first_index != second_index:
                    answer.append(first_index)
                    answer.append(second_index)
                    break
            if len(answer) == 2:
                break
        
        return answer
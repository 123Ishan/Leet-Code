class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
    
        my_string = "".join(map(str, digits))
        my_int = int(my_string) + 1
        new_string = str(my_int)
        final_array = [int(char) for char in new_string]
        return final_array
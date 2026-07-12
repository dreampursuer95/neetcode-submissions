class Solution:
    mapping = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"],
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        def get_combination(digits, index):
            if index == 0:
                return self.mapping[digits[index]]
            curr_combinations = get_combination(digits, index-1)
            res_list = []
            for comb in curr_combinations:
                for char in self.mapping[digits[index]]:
                    res_list.append(comb+char)
            return res_list
        return get_combination(digits, len(digits)-1)
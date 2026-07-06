class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, "032b")
        bits_str = str(bits)
        res_str = ""
        for char in bits_str:
            res_str = char + res_str
        return int(res_str, 2)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        place = len(digits) - 2
        while carry == 1 and place >= 0:
            print(place, carry)
            new = digits[place] + carry
            val, carry = new % 10, new // 10
            digits[place] = val
            place -= 1
        if place == -1 and carry == 1:
            return [1] + digits
        return digits




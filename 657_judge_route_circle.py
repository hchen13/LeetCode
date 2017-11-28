class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical_stack, horizontal_stack = 0, 0
        vertical_table = {
            "U": 1, "D": -1
        }
        horizontal_table = {
            "L": -1, "R": 1
        }
        for move in moves:
            if move in vertical_table:
                vertical_stack += vertical_table[move]
            elif move in horizontal_table:
                horizontal_stack += horizontal_table[move]
            else:
                raise ValueError("Invalid move: {}".format(move))
        return vertical_stack == 0 and horizontal_stack == 0


if __name__ == '__main__':
    solution = Solution()
    case = ["UD", "LL"]
    for test in case:
        answer = solution.judgeCircle(test)
        print("true" if answer else "false")

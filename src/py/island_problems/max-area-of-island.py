from typing import List


class Solution:
    def traverse(self, grid: List[List[int]], x: int, y: int):
        if x not in range(0, len(grid)) or y not in range(0, len(grid[x])):
            return 0

        if grid[x][y] == 2:
            return 0

        if grid[x][y] == 0:
            return 0

        if grid[x][y] == 1:
            grid[x][y] = 2
            return (1+self.traverse(grid, x - 1, y)
                    + self.traverse(grid, x + 1, y)
                    + self.traverse(grid, x, y - 1)
                    + self.traverse(grid, x, y + 1))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                max_area = max(max_area, self.traverse(grid, x, y))
        return max_area


if __name__ == '__main__':
    from collections import namedtuple

    TestCase = namedtuple('TestCae', field_names=['input', 'expect'])
    test_cases = [
        TestCase(
            input=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]],
            expect=6
        ),
        TestCase(
            input=[[0,0,0,0,0,0,0,0]],
            expect=0
        ),

    ]

    solution = Solution()
    for tc in test_cases:
        for i in tc.input:
            print(i)

        got = solution.maxAreaOfIsland(grid=tc.input)
        assert got == tc.expect, f"expect: {tc.expect}, got: {got}"

        print('=' * 30)

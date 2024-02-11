from typing import List


class Solution:
    def traverse(self, grid: List[List[int]], x: int, y: int, island_idx:int):
        if x not in range(0, len(grid)) or y not in range(0, len(grid[x])):
            return 0

        if grid[x][y] >= 2:
            return 0

        if grid[x][y] == 0:
            return 0

        if grid[x][y] == 1:
            grid[x][y] = island_idx
            return (1+self.traverse(grid, x - 1, y, island_idx=island_idx)
                    + self.traverse(grid, x + 1, y, island_idx=island_idx)
                    + self.traverse(grid, x, y - 1, island_idx=island_idx)
                    + self.traverse(grid, x, y + 1, island_idx=island_idx))

    def cal_island_area(self, grid: List[List[int]]) -> dict:
        island_idx = 1
        island_area = {}
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                if grid[x][y] == 1:
                    island_idx += 1
                    _area = self.traverse(grid, x, y, island_idx=island_idx)
                    island_area[island_idx] = _area
        return island_area

    def read_area(self,grid:List[List[int]],island_area:dict,x,y):
        if x not in range(0, len(grid)) or y not in range(0, len(grid[x])):
            return (0,0)
        return (grid[x][y], island_area.get(grid[x][y],0))

    def largestIsland(self, grid: List[List[int]]) -> int:
        island_area = self.cal_island_area(grid=grid)
        print("grid_assigned:")
        for i in grid:
            print(i)

        print(f"island_area: {island_area}")

        _max = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                if grid[x][y] == 0:
                    areas = [self.read_area(grid,island_area,x-1,y)
                    ,self.read_area(grid, island_area,x+1,y)
                    ,self.read_area(grid,island_area,x,y-1)
                    ,self.read_area(grid,island_area,x,y+1)]
                    connected_areas = {idx:area for idx,area in areas}
                    print(f"connected_areas: {connected_areas}")
                    area = 1+sum(connected_areas.values())
                    _max = max(_max,area)
        return max([_max]+list(island_area.values()))


if __name__ == '__main__':
    from collections import namedtuple

    TestCase = namedtuple('TestCae', field_names=['input', 'expect'])
    test_cases = [
        TestCase(
            input=[[1,0],[0,1]],
            expect=3
        ),
        TestCase(
            input=[[1,1],[1,0]],
            expect=4
        ),
        TestCase(
            input=[[1,1],[1,1]],
            expect=4
        ),
    ]

    solution = Solution()
    for tc in test_cases:
        for i in tc.input:
            print(i)

        got = solution.largestIsland(grid=tc.input)
        assert got == tc.expect, f"expect: {tc.expect}, got: {got}"

        print('=' * 30)

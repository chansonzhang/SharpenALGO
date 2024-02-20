import sys
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n_rows = len(maze)
        n_cols = len(maze[0])
        visited: List[List[bool]] = [[False] * n_cols for _ in range(n_rows)]
        status: List[List[int]] = [[-1] * n_cols for _ in range(n_rows)]
        start_x, start_y = start[0], start[1]
        destination_x, destination_y = destination[0], destination[1]
        for (i,j) in [(start_x - 1,start_y), (start_x + 1,start_y),
                      (start_x,start_y - 1), (start_x,start_y + 1),
                      ]:
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols:
                return -1
            if visited[i][j]:
                return status[i][j]
            min_dis = sys.maxsize
            dis = 0
            if i > start_x: #up
                ii = i
                while maze[ii][j] == 0:
                    dis += 1



if __name__ == "__main__":
    from collections import namedtuple

    TestCase = namedtuple("TestCase", field_names=["maze", "start", "destination", "expect"])
    test_cases: List[TestCase] = [
        TestCase(
            maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
            start=[0, 4], destination=[3, 2],
            expect=-1,
        ),
        TestCase(
            maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
            start=[0, 4], destination=[4, 4],
            expect=12,
        ),
        TestCase(
            maze=[[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]], start=[4, 3],
            destination=[0, 1]
            ,
            expect=-1
        ),
    ]
    solution = Solution()
    for tc in test_cases:
        got = solution.shortestDistance(maze=tc.maze, start=tc.start, destination=tc.destination)
        assert got == tc.expect, f"expect: {tc.expect}, got: {got}"
        print("#" * 30)

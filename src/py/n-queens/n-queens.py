from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        assignments: List[List[int]] = self.assign(n, n)
        rsts: List[List[str]] = []
        print(f"assignments: {assignments}")
        for a in assignments:
            assign_repr: List[str] = [''.join(['Q' if j == i else '.'
                                               for j in range(0, n)])
                                      for i in a]
            rsts.append(assign_repr)
        return rsts

    def assign(self, n: int, N: int) -> List[List[int]]:
        if n == 1:
            return [
                [i] for i in range(0, N)
            ]
        assignments_before = self.assign(n - 1, N)
        print(f"assignments_before: {assignments_before}")

        assignments = []
        for assign in assignments_before:
            for i in range(0, N):
                if i in assign:
                    continue
                conflict = False
                for row, j in enumerate(assign):
                    if abs(row + 1 - n) == abs(j - i):
                        conflict = True
                if conflict:
                    continue
                assignments.append(assign + [i])
        return assignments


if __name__ == "__main__":
    from collections import namedtuple

    TestCase = namedtuple('TestCase', field_names=['input', 'expect'])
    test_cases: List[TestCase] = [
        TestCase(
            input=4,
            expect=[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        ),
        TestCase(
            input=1,
            expect=[["Q"]]
        ),
    ]

    solution = Solution()
    for tc in test_cases:
        got = solution.solveNQueens(n=tc.input)
        assert got == tc.expect, f"expect: {tc.expect}, got: {got}"

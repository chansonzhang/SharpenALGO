from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        rst = [[0] * (len2 + 1) for _ in range(len1 + 1)] # +1 to handle index -1
        for i in range(0, len1):
            for j in range(0, len2):
                if text1[i] == text2[j]:
                    rst[i][j] = rst[i - 1][j - 1] + 1
                else:
                    rst[i][j] = max(rst[i - 1][j], rst[i][j - 1])
        return rst[len1 - 1][len2 - 1]


if __name__ == "__main__":
    from collections import namedtuple

    TestCase = namedtuple("TestCase", field_names=["text1", "text2", "expect"])
    test_cases: List[TestCase] = [
        TestCase(
            text1="abcde",
            text2="ace",
            expect=3
        ),
        TestCase(
            text1="abc", text2="abc",
            expect=3,
        ),
        TestCase(
            text1="abc", text2="def",
            expect=0
        ),
        TestCase(
            text1="oxcpqrsvwf",
            text2="shmtulqrypy",
            expect=2
        ),
    ]
    solution = Solution()
    for tc in test_cases:
        got = solution.longestCommonSubsequence(text1=tc.text1, text2=tc.text2)
        assert got == tc.expect, f"expect: {tc.expect}, got: {got}"
        print("#" * 30)

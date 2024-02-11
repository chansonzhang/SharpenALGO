from typing import List


class Solution:

    def update(self, pos_height: dict, left, right, side_len: int) -> set:
        keys_to_remove = set()
        find = False
        value_updates = {}
        for (start, end), height in pos_height.items():
            if right <= start:
                continue
            if end <= left:
                continue
            find = True
            keys_to_remove.add((start, end))
            # 移除当前段，拆分为 start-left, left-right, right-end 三段
            if left > start:
                height_left = value_updates[(start, left)] = height
            else:
                _, updates, height_left = self.update(pos_height, left, start, side_len)
                # left 覆盖了左端点，不用拆分

            if right < end:
                height_right = value_updates[(right, end)] = height
            else:
                _, updates, height_right = self.update(pos_height, end, right, side_len)
                # right 覆盖了右端点，不用拆分

            value_updates[(left, right)] = max([height + side_len,
                                                height_left,
                                                height_right])

        if not find:
            value_updates[(left, right)] = side_len

        updated_height = value_updates[(left, right)]
        return keys_to_remove, value_updates, updated_height

    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        pos_height = {}
        n = len(positions)
        ans = [0] * n
        for i, s in enumerate(positions):
            left = s[0]
            side_len = s[1]
            right = left + side_len
            find = False
            keys_to_remove, updates, updated_height = self.update(
                pos_height=pos_height,
                left=left,
                right=right,
                side_len=side_len)

            # print(f"keys_to_remove: {keys_to_remove}")
            for key in keys_to_remove:
                pos_height.pop(key)

            pos_height.update(updates)

            ans[i] = updated_height

            # print(f"pos_height: {dict(sorted(pos_height.items()))}")

        for i in range(1, len(positions)):
            ans[i] = max(ans[i], ans[i - 1])
        return ans


if __name__ == '__main__':
    from collections import namedtuple

    TestCase = namedtuple("TestCase", field_names=['input', 'expect'])
    test_cases = [
        TestCase(
            input=[[1, 2], [2, 3], [6, 1]],
            expect=[2, 5, 5],
        ),
        TestCase(
            input=[[100, 100], [200, 100]],
            expect=[100, 100],
        ),
        TestCase(
            input=[[50, 47], [95, 48], [88, 77], [84, 3], [53, 87], [98, 79], [88, 28], [13, 22], [53, 73], [85, 55]],
            expect=[47, 95, 172, 172, 259, 338, 366, 366, 439, 494],
        ),
    ]
    solution = Solution()
    for tc in test_cases:
        for i in tc.input:
            print(f"{(i[0], i[0]+i[1])}: {i[1]}")
        got = solution.fallingSquares(positions=tc.input)
        assert got == tc.expect, f"expect: {tc.expect}, got: {got}"
        print("=" * 30)

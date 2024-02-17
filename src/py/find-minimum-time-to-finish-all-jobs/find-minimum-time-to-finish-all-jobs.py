import sys
import time
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        POW_2_N = 1 << n
        cache = [[0] * POW_2_N for _ in range(k)]
        sums = [0] * POW_2_N

        time0 = time.time()
        for j in range(1, POW_2_N):
            trailing_zero_cnt = (j & -j).bit_length() - 1
            last_state = j - (1 << trailing_zero_cnt)
            sums[j] = sums[last_state] + jobs[trailing_zero_cnt]
            cache[0][j] = sums[j]

        cache[0][0] = sums[0]

        time1 = time.time()

        subs_of_j = [[] for _ in range(POW_2_N)]
        for j in range(POW_2_N):
            sub_j = j
            while sub_j != 0:
                subs_of_j[j].append(sub_j)
                sub_j = (sub_j - 1) & j

        time2 = time.time()
        for i in range(1, k):
            for j in range(POW_2_N):
                min_max_of_j = sys.maxsize
                for sub_j in subs_of_j[j]:
                    # 此处手写 if-else 比 max min 函数调用节省大量时间
                    if cache[i - 1][j - sub_j] > sums[sub_j]:
                        _max = cache[i - 1][j - sub_j]
                    else:
                        _max = sums[sub_j]
                    if _max < min_max_of_j:
                        min_max_of_j = _max
                cache[i][j] = min_max_of_j
        time3 = time.time()

        print(f"time1: {time1 - time0}")
        print(f"time2: {time2 - time1}")
        print(f"time3: {time3 - time2}")
        print(f"total: {time3 - time0}")
        return cache[k - 1][(POW_2_N) - 1]


if __name__ == '__main__':
    from collections import namedtuple

    TestCase = namedtuple('TestCase', field_names=['jobs', 'k', 'expect'])
    test_cases: List[TestCase] = [
        # TestCase(
        #     jobs=[3, 2, 3],
        #     k=3,
        #     expect=3
        # ),
        # TestCase(
        #     jobs=[1, 2, 4, 7, 8],
        #     k=2,
        #     expect=11
        # ),
        # TestCase(
        #     jobs=[9899456, 8291115, 9477657, 9288480, 5146275, 7697968, 8573153, 3582365, 3758448, 9881935, 2420271,
        #           4542202],
        #     k=9,
        #     expect=9899456
        # ),
        # TestCase(
        #     jobs=[331, 769, 967, 535, 243, 239, 529, 102, 250, 469, 261, 283],
        #     k=10,
        #     expect=967
        # ),
        TestCase(
            jobs=[643, 526, 589, 976, 986, 730, 345, 926, 798, 618, 827, 873],
            k=11,
            expect=986
        ),
    ]
    solution = Solution()
    for tc in test_cases:
        got = solution.minimumTimeRequired(jobs=tc.jobs, k=tc.k)
        assert got == tc.expect, f"expect: {tc.expect}, got: {got}"
        print("#" * 30)

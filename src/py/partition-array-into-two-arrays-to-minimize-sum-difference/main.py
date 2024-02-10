import sys
import time
from typing import List


class Solution:
    total_cal_cnt = 0
    cache_hit_cnt = 0

    def cal_sum(self, nums: List[int], k: int, cache) -> set:
        self.total_cal_cnt += 1
        tail_len = len(nums)
        # print(f'tail_len: {tail_len}, k: {k}, request')
        cached_rst = cache.get(tail_len, {}).get(k)
        if cached_rst is not None:
            self.cache_hit_cnt += 1
            # print(f'tail_len: {tail_len}, k: {k}, hit')
            return cached_rst

        if tail_len not in cache:
            cache[tail_len] = {}

        rst = None
        if k == 0:
            rst = {0}
        # elif k == 1:
        #     rst = set(nums)
        # elif len(nums) == k:
        #     rst = {sum(nums)}
        elif len(nums) < k:
            rst = {}

        if rst is not None:
            cache[tail_len][k] = rst
            # print(f'tail_len: {tail_len}, k: {k}, save')
            return rst

        sums = set()

        if k - 1 >= 0:
            sub_sums = self.cal_sum(nums=nums[1:], k=k - 1, cache=cache)
            for ss in sub_sums:
                sums.add(ss + nums[0])

        if tail_len >= 2:
            sum_sums = self.cal_sum(nums=nums[1:], k=k, cache=cache)
            for ss in sum_sums:
                sums.add(ss)
        cache[tail_len][k] = sums
        # print(f'tail_len: {tail_len}, k: {k}, save')
        return sums

    def cal_matrix(self, nums: List[int], cache) -> List[set]:
        n = len(nums)
        sums = [set()] * (n + 1)
        for k in range(0, n + 1):
            sums[k] = self.cal_sum(nums=nums, k=k, cache=cache)
        return sums

    def cal_matrix_with_cache(self, nums: List[int]):
        cache = {}
        return self.cal_matrix(nums=nums, cache=cache)

    def cal_matrix_dp(self, nums: List[int]):
        n = len(nums)
        cache = []
        for i in range(0, n + 1):
            cache.append([set()] * (n + 1))

        for i in range(0, len(cache)):
            cache[i][0] = {0}

        for k in range(1, len(cache)):
            cache[0][k] = set()
        # print(cache)
        for tail_len in range(1, len(nums) + 1):
            for k in range(1, tail_len + 1):
                rst = None
                if k == 0:
                    rst = {0}
                else:
                    # tail_len-1, k-1
                    if n - tail_len >= 0:
                        rst_with_current = {x + nums[n - tail_len] for x in cache[tail_len - 1][k - 1]}
                    else:
                        rst_with_current = set()
                    # tail_len-1, k
                    rst_without_current = cache[tail_len - 1][k]
                    # print(f"tail_len: {tail_len}, k: {k}")
                    rst = rst_with_current.union(rst_without_current)
                cache[tail_len][k] = rst
                # print(f"cache:")
                # for i in cache:
                #     print(i)

        # print(f"cache:")
        # for i in cache:
        #     print(i)
        return cache[n]

    def binary_search(self, nums, target, begin, end):
        if end == begin + 1:
            return nums[begin], abs(nums[begin]-target)
        if end <= begin:
            return sys.maxsize, sys.maxsize
        mid = begin + (end - begin) // 2
        if target == nums[mid]:
            return nums[mid], 0
        diff = abs(target - nums[mid])
        rst = nums[mid]
        if target < nums[mid]:
            rst1, diff1 = self.binary_search(nums=nums, target=target,
                                             begin=begin,
                                             end=mid)
        else:
            rst1, diff1 = self.binary_search(nums=nums, target=target,
                                             begin=mid + 1,
                                             end=end)
        if diff1 < diff:
            return rst1, diff1
        else:
            return rst, diff

    def minimumDifference(self, nums: List[int]) -> int:
        time0 = time.time()
        total_sum = sum(nums)
        target_sum = total_sum / 2
        print(f"target_sum: {target_sum}")
        n = len(nums) // 2
        nums = sorted(nums)
        left_nums = nums[0: n]
        right_nums = nums[n:]
        print(f"nums: {nums}")
        print(f"left_nums: {left_nums}")
        print(f"right_nums: {right_nums}")
        # dp 等价于递归+缓存，实际中 dp 内存占用较少
        # left_sums_matrix = self.cal_matrix_with_cache(nums=left_nums)
        left_sums_matrix = self.cal_matrix_dp(nums=left_nums)
        print('---------------' * 2)
        # right_sums_matrix = self.cal_matrix_with_cache(nums=right_nums)
        right_sums_matrix = self.cal_matrix_dp(nums=right_nums)
        # print(f"left_matrix: {left_sums_matrix}")
        # print(f"right_matrix: {right_sums_matrix}")
        closet_k = -1
        min_diff = sys.maxsize
        sum_with_min_diff = 0
        k_with_min_diff = 0
        sum1_with_min_diff = 0
        sum2_with_min_diff = 0
        time1 = time.time()
        print(f"time1-time0: {time1 - time0}")
        for k in range(0, n + 1):
            right_sums_matrix[k] = list(sorted(right_sums_matrix[k]))
        for k in range(0, n + 1):
            left_sums = left_sums_matrix[k]
            try:
                right_sums = right_sums_matrix[n - k]
            except IndexError as e:
                print(e)
                print(f"n:{n}, k: {k}, n-k: {n - k}, right_sums_matrix: {right_sums_matrix}")
            for ls in left_sums:
                expect_rs = target_sum - ls
                # print(f'right_sums: {right_sums}')
                # print(f"expect_rs:{expect_rs}")
                # print(f"len(right_sums): {len(right_sums)}")
                rs, _ = self.binary_search(nums=right_sums,
                                           target=expect_rs,
                                           begin=0,
                                           end=len(right_sums)
                                           )
                tmp_sum = ls + rs
                diff = abs(tmp_sum - target_sum)
                if diff < min_diff:
                    sum_with_min_diff = tmp_sum
                    min_diff = diff
            print('-' * 30)
        time2 = time.time()
        print(f'time2-time1: {time2 - time1}')
        print(f"sum_with_mini_diff: {sum_with_min_diff}")
        print(f"k_with_min_diff: {k_with_min_diff}")
        print(f"sum1: {sum1_with_min_diff}")
        print(f"sum2: {sum2_with_min_diff}")
        other_sum = total_sum - sum_with_min_diff
        return abs(other_sum - sum_with_min_diff)


if __name__ == '__main__':
    solution = Solution()
    from collections import namedtuple

    TestCase = namedtuple("TestCase", field_names=['nums', 'expect'])
    test_cases: List[TestCase] = [
        TestCase(nums=[3, 9, 7, 3], expect=2),
        TestCase(nums=[-36, 36], expect=72),
        TestCase(nums=[2, -1, 0, 4, -2, -9], expect=0),
        TestCase(nums=[76, 8, 45, 20, 74, 84, 28, 1], expect=2),
    ]

    for tc in test_cases:
        got = solution.minimumDifference(nums=tc.nums)
        assert got == tc.expect, (f"nums: {tc.nums}, "
                                  f"expect: {tc.expect}, "
                                  f"got: {got}")

    print(f"cal_cnt: {solution.total_cal_cnt}")
    print(f"cache_hit_cnt: {solution.cache_hit_cnt}")

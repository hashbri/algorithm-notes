# -*- coding: utf-8 -*-
"""
程序设计竞赛 · Python 速查模板（2026-10-14 学院校内赛）

用法：
    1) 直接运行本文件，看每个套路的实际输出：  python contest_io_template.py
    2) 比赛时，把需要的那个函数 / 那几行直接抄进你的答案里。

不要只读——照着敲一遍，敲三遍就进手了。
"""

import io
import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict


# ============================================================
# 1. 读入模板
# ============================================================

def read_line_int(text):
    """场景 A：一行一个整数。"""
    # 比赛里就是： n = int(input())
    return int(text.strip())


def read_two_ints(text):
    """场景 B：一行两个整数。 比赛里： a, b = map(int, input().split())"""
    a, b = map(int, text.split())
    return a, b


def read_int_list(text):
    """场景 B：一行一串整数变列表。 比赛里： arr = list(map(int, input().split()))"""
    return list(map(int, text.split()))


def read_all_tokens(text):
    """场景 C：一次性读全部空白分隔的内容（最稳）。
    比赛里： data = sys.stdin.read().split()  —— 快，且不怕换行位置怪。
    """
    return text.split()


def read_until_eof(lines):
    """场景 D：多组输入，读到文件结束。
    比赛里是 while True + try/except EOFError，这里用 lines 模拟输入流。
    """
    results = []
    for line in lines:
        line = line.strip()
        if line == "":
            break
        results.append(int(line))
    return results


# ============================================================
# 2. 列表 / 字典 / 字符串
# ============================================================

def demo_list_dict_str():
    arr = [3, 1, 4, 1, 5]
    arr.append(9)                      # [3,1,4,1,5,9]
    arr.sort()                         # 原地升序
    arr.sort(reverse=True)             # 降序
    b = sorted([3, 1, 4])              # 不改原列表

    d = {}
    d["apple"] = 3
    default = d.get("banana", 0)       # 取不到就给 0，省掉 if 判断

    s = "hello world"
    cnt = Counter(arr)                 # 一步统计词频
    return {
        "arr_after_sort_desc": arr,
        "sorted_new_list": b,
        "len/max/min/sum": (len(arr), max(arr), min(arr), sum(arr)),
        "reversed_slice": arr[::-1],
        "dict_default_get": default,
        "counter": dict(cnt),
        "most_common_1": cnt.most_common(1),
        "split/join": (s.split(), "-".join(s.split())),
        "upper/count/find": (s.upper(), s.count("l"), s.find("l")),
    }


# ============================================================
# 3. 排序（含多关键字）
# ============================================================

def sort_multi_key(students):
    """students: [(名字, 分数, 年龄)]，分数降序，分数相同年龄升序。"""
    return sorted(students, key=lambda x: (-x[1], x[2]))


# ============================================================
# 4. 查找与二分
# ============================================================

def count_occurrences(arr, x):
    """有序数组里 x 出现了几次：upper - lower（arr 必须已排序）。"""
    return bisect_right(arr, x) - bisect_left(arr, x)


def binary_search(arr, x):
    """手写二分：找到返回下标，否则返回 -1（arr 必须已排序）。"""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ============================================================
# 5. 前缀和
# ============================================================

def build_prefix(arr):
    """pre[i] = 前 i 个数之和（arr 从 0 开始编号）。"""
    pre = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        pre[i + 1] = pre[i] + arr[i]
    return pre


def range_sum(pre, l, r):
    """求 arr[l..r]（1 开始编号、含两端）的和。"""
    return pre[r] - pre[l - 1]


# ============================================================
# 6. 贪心
# ============================================================

def max_activities(acts):
    """活动安排：最多能参加几个互不重叠的活动。acts = [(开始, 结束)]。"""
    acts = sorted(acts, key=lambda x: x[1])   # 关键：按结束时间升序
    count, last_end = 0, -1
    picked = []
    for s, e in acts:
        if s >= last_end:
            count += 1
            picked.append((s, e))
            last_end = e
    return count, picked


# ============================================================
# 7. 动态规划（只背这 3 个）
# ============================================================

def dp_climb_stairs(n):
    """模板 1：爬楼梯。"""
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def dp_lis(arr):
    """模板 2：最长递增子序列长度。"""
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def dp_knapsack(weights, values, capacity):
    """模板 3：0-1 背包最大价值。"""
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for c in range(capacity, weights[i] - 1, -1):   # 注意倒着遍历
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i])
    return dp[capacity]


# ============================================================
# 演示
# ============================================================

def demo():
    print("=" * 56)
    print("1. 读入模板")
    print("=" * 56)
    print("读一行一个整数      :", read_line_int("42"))
    print("读一行两个整数      :", read_two_ints("3 5"))
    print("读一行变列表        :", read_int_list("1 2 3 4 5"))
    print("一次读全部 token    :", read_all_tokens("2\n3 4\n5 6"))
    print("读到 EOF（多组输入）:", read_until_eof(["7", "8", "9", ""]))

    print()
    print("=" * 56)
    print("2. 列表 / 字典 / 字符串")
    print("=" * 56)
    for k, v in demo_list_dict_str().items():
        print(f"  {k:22s} = {v}")

    print()
    print("=" * 56)
    print("3. 排序（多关键字）")
    print("=" * 56)
    students = [("Tom", 90, 18), ("Amy", 90, 17), ("Bob", 85, 19)]
    print("  原始          :", students)
    print("  分数降序+年龄升序:", sort_multi_key(students))

    print()
    print("=" * 56)
    print("4. 查找与二分")
    print("=" * 56)
    arr = [1, 2, 2, 2, 5, 8]
    print("  数组          :", arr)
    print("  8 的下标(手写二分):", binary_search(arr, 8))
    print("  2 出现次数(bisect):", count_occurrences(arr, 2))

    print()
    print("=" * 56)
    print("5. 前缀和")
    print("=" * 56)
    a = [3, 1, 4, 1, 5]
    pre = build_prefix(a)
    print("  数组          :", a)
    print("  前缀和        :", pre)
    print("  arr[2..4] 的和:", range_sum(pre, 2, 4), "(= 1+4+1 = 6)")

    print()
    print("=" * 56)
    print("6. 贪心：活动安排")
    print("=" * 56)
    acts = [(1, 3), (2, 4), (3, 5), (5, 7), (4, 6)]
    cnt, picked = max_activities(acts)
    print("  候选活动      :", acts)
    print("  最多能参加    :", cnt, "个 →", picked)

    print()
    print("=" * 56)
    print("7. 动态规划三个模板")
    print("=" * 56)
    print("  爬楼梯 n=5        :", dp_climb_stairs(5), "(1→2→3→5→8，第5级有8种走法)")
    print("  LIS [10,9,2,5,3,7,101]:", dp_lis([10, 9, 2, 5, 3, 7, 101]), "(= 4)")
    print("  0-1背包 w=[1,2,3] v=[6,10,12] C=5:", dp_knapsack([1, 2, 3], [6, 10, 12], 5), "(= 22)")

    print()
    print("=" * 56)
    print("提示：比赛时记得 sys.setrecursionlimit(100000) 防止递归爆栈")
    print("=" * 56)


if __name__ == "__main__":
    demo()

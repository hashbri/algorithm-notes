# -*- coding: utf-8 -*-
# 018_max_subarray.py —— 最大子段和（2026-11-02 加练）
#
# 这道题是专门来治「先攒后算」的。
#
# 规则（这次是真的硬性要求）：
#   1. **只许一个循环**。不许写双层 for。
#   2. **不许建列表**。没有 append，没有 []，不许把中间结果攒起来。
#   3. n 最多 10 万，双层循环必然超时（10^10 次）。自检的小用例测不出来，
#      但你写的是不是两层循环，我一眼看得到。
#
# 用法：
#   python 018_max_subarray.py        跑全部
#   python 018_max_subarray.py S1     只跑 S1


import io
import sys

FUNCS = {}


def problem(name):
    def deco(fn):
        FUNCS[name] = fn
        return fn
    return deco


# ======================================================================
# S1 · 最大子段和
# ======================================================================
# 【题面】
#   给 n 个整数（可能是负数），求「连续一段」的和里面最大的那个。
#   **至少要选一个数**，不能一个都不选。
#
# 【输入】
#   第 1 行：n
#   第 2 行：n 个整数（空格分隔）
# 【输出】
#   一个整数
#
# 【样例】
#   输入            输出
#   5               6
#   -2 3 -1 4 -3
#   （选 3 + (-1) + 4 = 6，这一段的右边那个 -3 不能要）
#
# 【提示】三个问题，想清楚就写出来了：
#   ① 你只需要**两个变量**。一个记什么？另一个记什么？
#   ② 如果前面那一段加起来已经是**负的**，把它接在当前数前面，
#      会让结果变大还是变小？想清楚这个，转移方式就有了。
#   ③ 这两个变量的**初值**给几？这题里给 0 会出事 —— 为什么？
@problem("S1")
def S1():
    n=int(input())
    a=list(map(int,input().split()))
    res=a[0]
    pos=0
    for i in a:
        pos=max(i,pos+i)
        res=max(res,pos)
    print(res)










# ======================================================================
# S2 · 买卖股票（变式：换了问法，但内核还是"边走边算"）
# ======================================================================
# 【题面】
#   给 n 天的股价。你只能**买一次、卖一次**，而且必须先买后卖。
#   求最大能赚多少。赚不到（一直跌）就输出 0。
#
# 【输入】
#   第 1 行：n
#   第 2 行：n 个整数（每天的股价）
# 【输出】一个整数
#
# 【样例】
#   输入                      输出
#   6                         5
#   7 1 5 3 6 4
#   （第 2 天 1 块买入，第 5 天 6 块卖出，赚 5）
#
# 【提示】三个问题：
#   ① 还是两个变量，但它们记的东西跟 S1 **不一样**。分别记什么？
#   ② 假设你正站在第 i 天，想立刻算出"今天卖掉能赚多少"，
#      你手上必须先知道哪个数？
#   ③ 那个数怎么一路维护下去？每走一天怎么更新它？
#
#   ⚠️ 不许用双层循环（n 到 10 万会超时），不许建列表。
@problem("S2")
def S2():
    n=int(input())
    data=list(map(int,input().split()))
    min_price=data[0]
    max_profit=0
    for i in data:
        if i<min_price:
            min_price=i
        max_=i-min_price
        if max_>max_profit:
            max_profit=max_
    print(max_profit)






# ======================================================================
# 自检
# ======================================================================

CHECKS = [
    ("S1", "5\n-2 3 -1 4 -3\n", "6"),
    ("S1", "1\n-5\n", "-5"),
    ("S1", "4\n-1 -2 -3 -4\n", "-1"),
    ("S1", "6\n1 -1 1 -1 1 -1\n", "1"),
    ("S1", "5\n5 4 -1 7 8\n", "23"),

    # ---- S2 买卖股票 ----
    ("S2", "6\n7 1 5 3 6 4\n", "5"),
    ("S2", "5\n7 6 4 3 1\n", "0"),
    ("S2", "2\n1 2\n", "1"),
    ("S2", "3\n2 4 1\n", "2"),
    ("S2", "3\n3 3 3\n", "0"),
    ("S2", "1\n5\n", "0"),
]


def self_check(only=None):
    total = ok = 0
    for name, fake_input, expected in CHECKS:
        if only and name != only:
            continue
        total += 1
        old_in, old_out = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(fake_input)
        buf = io.StringIO()
        sys.stdout = buf
        err = None
        try:
            FUNCS[name]()
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
        finally:
            sys.stdin, sys.stdout = old_in, old_out

        if err:
            print(f"  {name}  x 报错 -> {err}")
            continue

        actual = buf.getvalue().replace("\r\n", "\n").rstrip("\n")
        exp = expected.rstrip("\n")
        if actual == exp:
            ok += 1
            print(f"  {name}  ✓ 通过")
        else:
            print(f"  {name}  ✗ 未过")
            print(f"       输入: {fake_input!r}")
            print(f"       期望: {exp!r}")
            print(f"       实际: {actual!r}")

    print()
    print(f"总计 {ok} / {total}")


if __name__ == "__main__":
    self_check(sys.argv[1] if len(sys.argv) > 1 else None)

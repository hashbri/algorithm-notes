# -*- coding: utf-8 -*-
# 030_retest.py —— 双指针回炉卷（2026-11-15 周日）
#
# 为什么单独建这个文件：
#   029 里有题面提示、有骨架、有自己写过的代码 —— 在那儿重写等于抄。
#   这份什么都没有：只有题面 + 硬要求 + 用例。
#
# 规则（自己守）：
#   1. 不许打开 029；不许看 git 历史；不许问我
#   2. 两题各限时 20 分钟
#   3. 全绿之后再跟 029 对照，看写法差在哪
#
# 用法：
#   python 030_retest.py          跑全部
#   python 030_retest.py R2       只跑 R2

import io
import sys

FUNCS = {}


def problem(name):
    def deco(fn):
        FUNCS[name] = fn
        return fn
    return deco


# ======================================================================
# R2 · 原地去重
# ======================================================================
# 【题面】
#   给一个升序数组，把重复的去掉，结果保存在原数组本身里。
#   输出两行：
#     第 1 行：去重后剩几个数
#     第 2 行：数组的前 k 个位置
#     1 1 2 3 3 3 3
#
# 【输入】第 1 行 n；第 2 行 n 个升序整数（可能有重复）
#
# 【硬要求】
#   1. 不许新建列表装结果；不许 set；不许 sorted(set())
#   2. 单层循环，只走一遍
#   3. 整体 O(n) —— 想一想：哪些操作内部本身就是一层循环？
@problem("R2")
def R2():
    n = int(input())
    a = list(map(int, input().split()))
    i,j=0,1
    while j<n:
        if a[i]!=a[j]:
            i+=1
            a[i]=a[j]
            j+=1
        else:
            j+=1
    print(i+1)
    print(*a[:i+1])

    # 白纸


# ======================================================================
# R5 · 和 ≥ target 的最短连续子数组
# ======================================================================
# 【题面】
#   给 n 个正整数和 target，找最短的连续段使它的和 ≥ target，输出这个长度。
#   找不到输出 0。
#
# 【输入】第 1 行 n target；第 2 行 n 个正整数
#
# 【硬要求】
#   1. 滑动窗口，整体 O(n)
#   2. 不许双层循环
@problem("R5")
def R5():
    n, target = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a=0
    i=0
    min_a=n+1
    for j in range(n):
        sum_a+=a[j]
        while sum_a>=target:
            res=j-i+1
            if res<min_a:
                min_a=res
            sum_a-=a[i]
            i+=1
    if min_a==n+1:
        min_a=0
    print(min_a)


    # 白纸


# ======================================================================
# R6 · 变式：和 ≤ target 的最长连续段
# ======================================================================
# 【为什么加这题】
#   R5 你看了旧代码才写出来。这题结构几乎一样，但**条件是反的** ——
#   套模板必错，只有真理解"什么时候缩窗口"才能写出来。
#
# 【题面】
#   给 n 个正整数和 target，找**和 ≤ target 的最长连续段**，输出这个长度。
#   如果连单个元素都比 target 大（一个都选不了），输出 0。
#
# 【输入】第 1 行 n target；第 2 行 n 个正整数
#
# 【例】
#   5 6
#   1 2 3 4 5
#   →  3      （1+2+3=6 ≤ 6；再加 4 就 10 超了）
#
# 【硬要求】
#   1. 滑动窗口，整体 O(n)
#   2. 不许双层循环
#
# 【就该想的那个问题】
#   R5 是"和**够了**就缩"，这题呢？是"和**超了**才缩"。
#   为什么两个方向都成立？—— 因为它们吃的是同一个前提。
@problem("R6")
def R6():
    n, target = map(int, input().split())
    a = list(map(int, input().split()))
    i=0
    sum_a=0
    max_a=0
    for j in range(n):
        sum_a+=a[j]
        while sum_a>target:
            sum_a-=a[i]
            i+=1
        res=j-i+1
        if res>max_a:
            max_a=res
    print(max_a)


    # 白纸


# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    ("R2", "6\n1 1 2 3 3 3\n", "3\n1 2 3"),
    ("R2", "5\n7 7 7 7 7\n", "1\n7"),
    ("R2", "1\n5\n", "1\n5"),
    ("R2", "5\n1 2 3 4 4\n", "4\n1 2 3 4"),

    ("R5", "6 7\n2 3 1 2 4 3\n", "2"),
    ("R5", "5 100\n1 2 3 4 5\n", "0"),
    ("R5", "5 15\n1 2 3 4 5\n", "5"),
    ("R5", "8 12\n10 1 1 1 1 1 1 10\n", "3"),

    ("R6", "5 6\n1 2 3 4 5\n", "3"),
    ("R6", "4 2\n1 1 1 1\n", "2"),
    ("R6", "1 3\n5\n", "0"),
    ("R6", "3 6\n2 2 2\n", "3"),
    ("R6", "5 15\n1 2 3 4 5\n", "5"),
    ("R6", "4 3\n10 1 1 1\n", "3"),
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

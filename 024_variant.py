# -*- coding: utf-8 -*-
# 024_variant.py —— 变式题（2026-11-11 周三）
#
# 昨天做的 R3/R4 是同一个内核：**边走边算 + 打擂台**。
# 今天两道题内核没变，换了两样东西：
#   V1：换判断条件（从"相等"变成"更大"）
#   V2：加一个任务（擂主要记住"自己在哪"）
#
# ★ 两条硬规矩（今天就是为了治这两个毛病）：
#   1. **禁用 max()**，只能用 if 比。你已经会"边走边算"了，
#      但昨天化简后还在借 max()。自己写一遍比较，才知道擂主是怎么更新的。
#   2. **不许建列表、不许 append**（先攒后算，第 6 次机会）
#
# 用法：
#   python 024_variant.py         跑全部
#   python 024_variant.py V1      只跑 V1

import io
import sys

FUNCS = {}


def problem(name):
    def deco(fn):
        FUNCS[name] = fn
        return fn
    return deco


# ======================================================================
# V1 · 最长连续递增段
# ======================================================================
# 【题面】
#   读入一行整数，输出「连续递增」最长那一段的长度。
#   递增的意思是**严格变大**（后一个 > 前一个），相等不算。
#
# 【输入】一行整数
# 【输出】一个整数（至少是 1）
#
# 【例】
#   1 2 3 1 2 3 4 5   →  5   （1 2 3 4 5 这一段）
#   5 4 3 2 1         →  1   （一个都不递增，每段都只有 1 个）
#   1 1 1             →  1   （相等不算递增）
#
# 【提示】这题的结构跟昨天的 R4 一模一样，只有一处不同：
#   ① R4 的判断是 data[i] == data[i-1]，这题是什么？
#   ② 两个变量的初值给几？（输出至少是 1 说明什么）
#   ③ "当前段长"什么时候归 1？
#
#   ⚠️ 不许用 max()，自己写 if 比。
@problem("V1")
def V1():
    data=list(map(int,input().split()))
    c=1
    best=1
    for i in range(0,len(data)-1):
        if data[i+1]>data[i]:
            c+=1
        else:
            c=1
        if best < c:
            best = c
    print(best)


# ======================================================================
# V2 · 相邻差最大的那一对，在哪？
# ======================================================================
# 【题面】
#   读入一行整数（至少 2 个），找出「相邻两项之差的绝对值」最大的那一对，
#   输出它们的**位置**（从 1 开始数）和这个差，空格隔开。
#   如果有并列最大的，输出**第一次出现**的那一对。
#
# 【输入】一行整数（n ≥ 2）
# 【输出】三个整数：前一个的位置、后一个的位置、差值
#
# 【例】
#   3 7 2 9   →  3 4 7
#   相邻差：|7-3|=4、|2-7|=5、|9-2|=7
#   最大是 7，落在第 3 个数和第 4 个数之间 → 输出 "3 4 7"
#
#   -5 5      →  1 2 10
#
# 【提示】这题比 R3 多一件事：**擂主不能只记"多大"，还要记"它在哪"**。
#   ① 你要几个变量？分别记什么？
#   ② 擂主的初值给几？（差值最小可能是多少？）
#   ③ 擂台被打赢的时候，除了更新最大值，还要干什么？
#      —— 想一想：如果只更新了最大值、忘了更新位置，会发生什么？
#
#   ⚠️ 不许用 max()，自己写 if 比。
@problem("V2")
def V2():
    data=list(map(int,input().split()))
    a=[0]+data
    best=0
    o,p=2,1
    for i in range(1,len(data)):
        c=abs(a[i+1]-a[i])
        if c>best:
            best=c
            o,p=i+1,i

    print(p,o,best)


# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    # ---- V1 最长连续递增段 ----
    ("V1", "1 2 3 1 2 3 4 5\n", "5"),
    ("V1", "5\n", "1"),
    ("V1", "5 4 3 2 1\n", "1"),
    ("V1", "1 1 1\n", "1"),
    ("V1", "1 2 3 4\n", "4"),

    # ---- V2 相邻差最大的一对 ----
    ("V2", "3 7 2 9\n", "3 4 7"),
    ("V2", "1 5\n", "1 2 4"),
    ("V2", "5 5 5\n", "1 2 0"),
    ("V2", "10 1 10 1\n", "1 2 9"),
    ("V2", "-5 5\n", "1 2 10"),
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

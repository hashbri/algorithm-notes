# -*- coding: utf-8 -*-
# 021_ascii_count.py —— ASCII + 计数数组（2026-11-07）
#
# L1 缺口第 2 项：ASCII。
# 这题把三样东西串在一起：
#   1. ord(c) - 97  把字母变成 0~25 的下标
#   2. 计数数组必须**先初始化**（append 做不到随机下标累加）
#   3. 按下标顺序输出 = 自动按字母表顺序
#
# 用法：
#   python 021_ascii_count.py


import io
import sys


# ======================================================================
# 题面
# ======================================================================
#
# 【题目】字母频率
#
#   读入一行**只含小写字母**的字符串，按字母表顺序输出
#   **出现过的**字母和它出现的次数，格式：字母 空格 次数
#
# 【输入】一行字符串（长度 1 ~ 10^5）
# 【输出】若干行，每行「字母 次数」
#
# 【样例】
#   输入          输出
#   banana        a 3
#                 b 1
#                 n 2
#
# 【提示】
#   ① 先建一个长度 26 的计数数组，全 0。
#      **必须初始化** —— 你不知道字母会按什么顺序来，
#      append 只能按顺序加，随机下标累加必须先有一排现成的格子。
#   ② 字母 c 转下标：ord(c) - 97（'a' 的编码是 97）。
#   ③ 输出时从 0 到 25 扫一遍计数数组，非 0 的输出 chr(97 + i)。
#      这样自然就是字母表顺序，不用再排序。
#
# ----------------------------------------------------------------------
# 在下面的函数里写：
# ----------------------------------------------------------------------

def solve():
    n=input()
    cnt=[0]*26
    for i in n:
        s=ord(i)-97
        cnt[s]+=1
    for h in range(26):
        if cnt[h]!=0:
            print(chr(97+h),cnt[h])



# ======================================================================
# 自检（别改）
# ======================================================================

CHECKS = [
    ("banana\n", "a 3\nb 1\nn 2"),
    ("abc\n", "a 1\nb 1\nc 1"),
    ("zzzz\n", "z 4"),
    ("a\n", "a 1"),
    ("abccba\n", "a 2\nb 2\nc 2"),
]


def self_check():
    ok = 0
    for i, (fake_input, expected) in enumerate(CHECKS, 1):
        old_in, old_out = sys.stdin, sys.stdout
        sys.stdin = io.StringIO(fake_input)
        buf = io.StringIO()
        sys.stdout = buf
        err = None
        try:
            solve()
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
        finally:
            sys.stdin, sys.stdout = old_in, old_out

        if err:
            print(f"  用例 {i}  x 报错 -> {err}")
            continue

        actual = buf.getvalue().replace("\r\n", "\n").rstrip("\n")
        exp = expected.rstrip("\n")
        if actual == exp:
            ok += 1
            print(f"  用例 {i}  ✓ 通过")
        else:
            print(f"  用例 {i}  ✗ 未过")
            print(f"       输入: {fake_input!r}")
            print(f"       期望: {exp!r}")
            print(f"       实际: {actual!r}")

    print()
    print(f"总计 {ok} / {len(CHECKS)}")


if __name__ == "__main__":
    self_check()
